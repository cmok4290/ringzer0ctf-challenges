#!/usr/bin/env python
from utils.constants import URL
import utils.challenge as c
import requests
import time


def main():
    prog_start = time.time()

    session = requests.Session()
    cookie = c.get_cookie('config.json')

    challenge, messages = c.get_challenge(session, URL, 13, cookie)
    # print(challenge)
    # print(messages)

    cha_start = time.time()
    seconds = c.get_seconds(challenge.contents[1])
    algorithm = c.get_algorithm(challenge.contents[1])
    payload = c.get_hash(algorithm, messages[0])
    flag = c.post_challenge(session, URL, 13, cookie, payload)
    print(flag)

    cha_end = time.time() - cha_start
    print(f'challenge: {seconds}s')
    print(f'actual: {round(cha_end, 3)}s')

    prog_end = time.time() - prog_start
    print(f'total: {round(prog_end, 3)}s')


if __name__ == '__main__':
    main()
