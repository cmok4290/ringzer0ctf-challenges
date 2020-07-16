#!/usr/bin/env python
from lib.challenge import Challenge
import time


def main():
    start = time.time()

    challenge = Challenge(14)
    message = challenge.get_challenge()
    print(message)
    message = ''.join([chr(int(message[i:i+8], 2))
                       for i in range(0, len(message), 8)])
    hashed_message = challenge.get_hash("sha512", message)
    print(hashed_message)
    flag = challenge.post_challenge(hashed_message)
    print(flag)

    end = time.time() - start
    print(round(end, 3), 's')


if __name__ == '__main__':
    main()
