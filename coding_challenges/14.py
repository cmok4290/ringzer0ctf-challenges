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
    url = 'https://ringzer0ctf.com/challenges/14'

    with open('config.json', 'r') as f:
        config = json.load(f)

    cookie = {"PHPSESSID": config["PHPSESSID"]}
    regex = re.compile(r'[\n\r\t]')

    # initial request
    r = s.get(url, cookies=cookie)
    start = time.time()

    # retrieve message
    soup = BeautifulSoup(r.content, features="lxml")
    tag = soup.find("div", class_="message")
    message = tag.contents[2]
    message = regex.sub("", message)
    # group bits into bytes or 8 bits
    # convert bytes to integers then characters
    message = ''.join([chr(int(message[i:i+8], 2))
                       for i in range(0, len(message), 8)])

    # create hash
    hashed = hashlib.sha512(message.encode('utf-8')).hexdigest()

    # submit hash
    r = s.get(f'{url}/{hashed}', cookies=cookie)
    soup = BeautifulSoup(r.content, features="lxml")

    # retrieve challenge flag
    tag = soup.find("div", class_="alert alert-info")
    flag = tag.contents[0]
    print(flag)
    end = time.time() - start
    print(round(end, 3), 's')


if __name__ == '__main__':
    main()
