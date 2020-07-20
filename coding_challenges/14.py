#!/usr/bin/env python
from dotenv import load_dotenv
import hashlib
import os
import re
import requests
import sys

load_dotenv()

LOGIN = 'https://ringzer0ctf.com/login'
CHALLENGE = 'https://ringzer0ctf.com/challenges/' + sys.argv[0].split('.')[0]


def get_hash(password, hash_type='sha512'):
    if hash_type in hashlib.algorithms_available:
        h = hashlib.new(hash_type)
        h.update(password.encode('utf-8'))
        return h.hexdigest()
    return None


def main():
    credentials = {'username': os.getenv(
        'RZ_CTF_USER'), 'password': os.getenv('RZ_CTF_PASS')}

    with requests.Session() as s:
        post_res = s.post(LOGIN, data={'username': os.getenv(
            'RZ_CTF_USER'), 'password': os.getenv('RZ_CTF_PASS')})

        if post_res:
            get_res = s.get(CHALLENGE)

        if get_res:
            # print(get_res.text)
            message_match = re.search(
                r'(?<=----- BEGIN MESSAGE -----<br \/>\r\n\t\t)(.*)(?=<br \/>\r\n\t\t----- END MESSAGE -----)', get_res.text)
            # print(message_match.group(0))
            bin_message = message_match.group(0)
            message = [chr(int(bin_message[i:i+8], 2))
                       for i in range(0, len(bin_message), 8)]
            message = ''.join(message)
            hashed_pw = get_hash(message)
            # print(secret)
            if hashed_pw is not None:
                flag_res = s.get(CHALLENGE + '/' + hashed_pw)
            else:
                print('hash not created, try again')
                exit(0)

        if flag_res:
            flag_match = re.search(r'FLAG-[a-zA-Z0-9]+', flag_res.text)
            print(flag_match.group(0))


if __name__ == '__main__':
    main()
