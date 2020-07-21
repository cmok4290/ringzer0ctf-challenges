#!/usr/bin/env python
# coding_challenges/hash_breaker.py
from dotenv import load_dotenv
import hashlib
import os
import re
import requests

load_dotenv()

LOGIN = 'https://ringzer0ctf.com/login'
CHALLENGE = 'https://ringzer0ctf.com/challenges/56'
COMMON_PASSWORDS = requests.get(
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').text.split('\n')


def brute_force(hash_str, salt_str=None, hash_type='sha1'):
    for password in COMMON_PASSWORDS:
        h = hashlib.new(hash_type)
        enc_pass = password.encode('utf-8')
        if salt_str is not None:
            enc_salt = salt_str.encode('utf-8')
            h.update(enc_pass+enc_salt)
        else:
            h.update(enc_pass)
        if h.hexdigest() == hash_str:
            return password
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
            hash_match = re.search(
                r'(?<=----- BEGIN HASH -----<br \/>\r\n\t\t)(.*)(?=<br \/>\r\n\t\t----- END HASH -----)', get_res.text)
            # print(hash_match.group(0))
            salt_match = re.search(
                r'(?<=----- BEGIN SALT -----<br \/>\r\n\t\t)(.*)(?=<br \/>\r\n\t\t----- END SALT -----)', get_res.text)
            # print(salt_match.group(0))
            secret = brute_force(hash_match.group(0))
            # print(secret)
            if secret is not None:
                flag_res = s.get(CHALLENGE + '/' + secret)
            else:
                print('secret not found, try again')
                exit(0)

        if flag_res:
            flag_match = re.search(r'FLAG-[a-zA-Z0-9]+', flag_res.text)
            flag = flag_match.group(0)
            print(flag)
    return flag


if __name__ == '__main__':
    main()
