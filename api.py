# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file....
"""

import requests

def get_fact(number):
    url = "http://numbersapi.com/{}".format(number)

    r = requests.get(url,timeout=3)
    if r.status_code == 200:
        print(r.text)
    else:
        print("An error occurred, code={}".format(r.status_code))
