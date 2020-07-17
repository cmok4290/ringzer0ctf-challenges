#!/usr/bin/env python
from bs4 import BeautifulSoup
import hashlib
import json
import re
import requests


def get_cookie(file_path):
    with open(file_path, 'r') as f:
        cookie = json.load(f)
    return cookie


def get_challenge(session, url, challenge_id, cookie):
    cha_url = f'{url}/{challenge_id}'
    res = session.get(cha_url, cookies=cookie)
    soup = BeautifulSoup(res.content, features='lxml')
    challenge = soup.find('div', class_='challenge-wrapper')
    messages = []
    regex = re.compile(r'[\n\r\t]')
    for message in soup.find_all('div', class_='message'):
        m = regex.sub('', message.contents[2])
        messages += [m]
    return (challenge, messages)


def get_seconds(html):
    contents = html.contents[0]
    regex = re.compile(r'[0-9]+(?=\sseconds)')
    result = regex.search(contents)
    seconds = result.group(0)
    return seconds


def get_algorithm(html):
    contents = html.contents[0]
    regex = re.compile(r'[a-z0-9_]+(?=\salgorithm)')
    result = regex.search(contents)
    algorithm = result.group(0)
    return algorithm


def get_hash(algorithm, string):
    try:
        h = hashlib.new(algorithm)
        b_string = string.encode('utf-8')
        h.update(b_string)
        if algorithm.startswith('shake'):
            length = algorithm.split('_')[-1]
            return h.hexdigest(length)
        return h.hexdigest()
    except ValueError as e:
        print(e)


def post_challenge(session, url, challenge_id, cookie, data):
    cha_url = f'{url}/{challenge_id}/{data}'
    res = session.get(cha_url, cookies=cookie)
    soup = BeautifulSoup(res.content, features='lxml')
    flag = soup.find('div', class_='alert alert-info')
    return flag.contents[0]


def str_to_int(s):
    # is binary?
    s_set = set(s)
    binary = {"0", "1"}
    if s_set == binary or s_set == {"0"} or s_set == {"1"}:
        return int(s, 2)
    # is hex?
    if s.startswith('0x'):
        return int(s, 16)
    # is int?
    if s.isnumeric():
        return int(s, 10)
