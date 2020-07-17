#!/usr/bin/env python
from utils.constants import URL
from utils.hash_decryptor import Decryptor
import utils.challenge as c
import requests
import time
import sys


def main():
    prog_start = time.time()
    challenge_id = sys.argv[0].split('.')[0]

    session = requests.Session()
    cookie = c.get_cookie('config.json')

    challenge, messages = c.get_challenge(session, URL, challenge_id, cookie)
    # print(challenge)
    # print(messages)

    cha_start = time.time()
    seconds = c.get_seconds(challenge.contents[1])
    payload = Decryptor(messages[0]).decrypt()
    flag = c.post_challenge(session, URL, challenge_id, cookie, payload)
    print(flag)

    cha_end = time.time() - cha_start
    print(f'challenge: {seconds}s')
    print(f'actual: {round(cha_end, 3)}s')

    prog_end = time.time() - prog_start
    print(f'total: {round(prog_end, 3)}s')


if __name__ == '__main__':
    main()
