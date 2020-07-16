#!/usr/bin/env python
from bs4 import BeautifulSoup
import hashlib
import json
import re
import requests


class Challenge:
    def __init__(self, ch_id):
        self.ch_id = ch_id
        self.config = None
        self.session = requests.Session()
        self.url = 'https://ringzer0ctf.com/challenges'

    def _get_config(self):
        if self.config == None:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        return self.config

    def _get_soup_tag(self, url, cookie, element, class_name):
        res = self.session.get(url, cookies=cookie)
        # print(res.content)
        soup = BeautifulSoup(res.content, features="lxml")
        tag = soup.find(element, class_=class_name)
        return tag

    def get_challenge(self):
        url = f'{self.url}/{self.ch_id}'
        config = self._get_config()
        regex = re.compile(r'[\n\r\t]')
        tag = self._get_soup_tag(url, self._get_config(), "div", "message")
        msg = tag.contents[2]
        msg = regex.sub("", msg)
        return msg

    def get_hash(self, algo, msg):
        if algo in hashlib.algorithms_available:
            h = hashlib.new(algo)
            enc_msg = msg.encode("utf-8")
            h.update(enc_msg)
            return h.hexdigest()

    def post_challenge(self, data):
        url = f'{self.url}/{self.ch_id}/{data}'
        config = self._get_config()
        tag = self._get_soup_tag(
            url, self._get_config(), "div", "alert alert-info")
        flag = tag.contents[0]
        return flag
