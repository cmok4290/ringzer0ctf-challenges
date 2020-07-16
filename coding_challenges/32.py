#!/usr/bin/env python
from lib.challenge import Challenge
import operator
import time


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


def main():
    start = time.time()

    challenge = Challenge(32)
    message = challenge.get_challenge()
    # print(message)
    message = message.split(" ")
    # print(message)
    ops = {
        "+": operator.add,
        "-": operator.sub
    }
    # quick maths
    a = str_to_int(message[0])
    b = str_to_int(message[2])
    c = str_to_int(message[4])
    total = ops[message[1]](a, b)
    total = ops[message[3]](total, c)
    # print(total)

    data = str(total)
    # print(data)
    flag = challenge.post_challenge(data)
    print(flag)

    end = time.time() - start
    print(round(end, 3), 's')


if __name__ == '__main__':
    main()
