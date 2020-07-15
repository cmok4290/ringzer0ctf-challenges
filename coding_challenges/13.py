#!/usr/bin/env python
from bs4 import BeautifulSoup
import hashlib
import json
import re
import requests
import time


def main():
    # initial config
    s = requests.Session()
    url = 'https://ringzer0ctf.com/challenges/13'

    with open('config.json', 'r') as f:
        config = json.load(f)

    cookie = {"PHPSESSID": config["PHPSESSID"]}
    regex = re.compile(r'[\n\r\t]')

    # initial request
    r = s.get(url, cookies=cookie)
    start = time.time()
    soup = BeautifulSoup(r.text, features="lxml")

    # retrieve message
    tag = soup.find("div", class_="message")
    message = tag.contents[2]
    message = regex.sub("", message)

    # create hash
    hashed = hashlib.sha512(message.encode()).hexdigest()

    # submit hash
    r = s.get(f'{url}/{hashed}', cookies=cookie)
    soup = BeautifulSoup(r.text, features="lxml")

    # retrieve challenge flag
    tag = soup.find("div", class_="alert alert-info")
    flag = tag.contents[0]
    print(flag)
    end = time.time() - start
    print(round(end, 3), 's')


if __name__ == '__main__':
    main()
