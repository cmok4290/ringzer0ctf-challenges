#!/usr/bin/env python
from utils.constants import URL
import utils.challenge as c
import operator
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
    message = messages[0].split(' ')

    ops = {
        "+": operator.add,
        "-": operator.sub
    }
    # quick maths
    x = c.str_to_int(message[0])
    y = c.str_to_int(message[2])
    z = c.str_to_int(message[4])
    total = ops[message[1]](x, y)
    total = ops[message[3]](total, z)

    cha_start = time.time()
    seconds = c.get_seconds(challenge.contents[3])
    payload = str(total)
    flag = c.post_challenge(session, URL, challenge_id, cookie, payload)
    print(flag)

    cha_end = time.time() - cha_start
    print(f'challenge: {seconds}s')
    print(f'actual: {round(cha_end, 3)}s')

    prog_end = time.time() - prog_start
    print(f'total: {round(prog_end, 3)}s')


if __name__ == '__main__':
    main()
