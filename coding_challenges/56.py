#!/usr/bin/env python
from lib.challenge import Challenge
from lib.hash_decryptor import Decryptor

def main():
    c = Challenge(56)
    msg = c.get_challenge()
    d = Decryptor(msg)
    decrypted = d.decrypt()
    flag = c.post_challenge(decrypted)
    print(flag)

if __name__ == '__main__':
    main()
