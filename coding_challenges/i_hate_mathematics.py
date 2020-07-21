#!/usr/bin/env python
import hashlib
import json
import operator
import os
import re
import requests

LOGIN = 'https://ringzer0ctf.com/login'
CHALLENGE = 'https://ringzer0ctf.com/challenges/32'
OPS = {'+': operator.add, '-': operator.sub}

with open('config.json', 'r') as f:
    DATA = json.load(f)


def to_int(s):
    s_set = set(s)
    binary = {'0', '1'}
    if s_set == binary or s_set == {'0'} or s_set == {'1'}:
        return int(s, 2)
    if s.startswith('0x'):
        return int(s, 16)
    if s.isnumeric():
        return int(s, 10)
    return None


def main():
    with requests.Session() as s:
        post_res = s.post(LOGIN, data=DATA)

        if post_res:
            get_res = s.get(CHALLENGE)

        if get_res:
            # print(get_res.text)
            message_match = re.search(
                r'(?<=----- BEGIN MESSAGE -----<br \/>\r\n\t\t)(.*)(?=<br \/>\r\n\t\t----- END MESSAGE -----)', get_res.text)
            # print(message_match.group(0))
            data = message_match.group(0).split(' ')
            a = to_int(data[0])
            b = to_int(data[2])
            c = to_int(data[4])
            if type(a) is type(b) is type(c) is int:
                total = OPS[data[1]](a, b)
                total = OPS[data[3]](total, c)
                # print(total)
                flag_res = s.get(CHALLENGE + '/' + str(total))
            else:
                print('str not converted to int, try again')
                exit(0)

        if flag_res:
            flag_match = re.search(r'FLAG-[a-zA-Z0-9]+', flag_res.text)
            flag = flag_match.group(0)
            print(flag_match.group(0))
    return flag


if __name__ == '__main__':
    main()
