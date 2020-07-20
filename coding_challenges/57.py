#!/usr/bin/env python
from dotenv import load_dotenv
import hashlib
import os
import re
import requests

load_dotenv()

LOGIN = 'https://ringzer0ctf.com/login'
CHALLENGE = 'https://ringzer0ctf.com/challenges/57'
COMMON_PASSWORDS = requests.get(
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').text.split('\n')


def brute_force(hash_str, salt_str, hash_type='sha1'):
    for password in COMMON_PASSWORDS:
        h = hashlib.new(hash_type)
        h.update(password.encode('utf-8')+salt_str.encode('utf-8'))
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
            secret = brute_force(hash_match.group(0), salt_match.group(0))
            # print(secret)
            if secret is not None:
                flag_res = s.get(CHALLENGE + '/' + secret)
            else:
                print('secret not found, try again')
                exit(0)

        if flag_res:
            flag_match = re.search(r'FLAG-[a-zA-Z0-9]+', flag_res.text)
            print(flag_match.group(0))


if __name__ == '__main__':
    main()
