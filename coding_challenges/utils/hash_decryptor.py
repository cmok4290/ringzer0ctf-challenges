#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests


class Decryptor:
    def __init__(self, data):
        self.apis = ['https://hashtoolkit.com/decrypt-hash/?hash=']
        self.data = data
        self.headers = {
            'User-Agent': 'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)'
        }
        self.session = requests.Session()

    def decrypt(self):
        for api in self.apis:
            response = self.session.get(api + self.data, headers=self.headers)
            if response:
                soup = BeautifulSoup(response.content, features="lxml")
                for a in soup.find_all('a', href=True):
                    if a['href'].startswith('/generate-hash/?text='):
                        return a.contents[0]
