#!/usr/bin/env python
from urllib.request import urlopen

COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8').split('\n')
CHALLENGES = 'https://ringzer0ctf.com/challenges'
LOGIN = 'https://ringzer0ctf.com/login'
