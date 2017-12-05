#!/usr/bin/env python
# -*- coding = utf-8 -*-

import requests

def main():
    r = requests.get("http://www.baidu.com")
    p = r.text
    print(p)
main()
