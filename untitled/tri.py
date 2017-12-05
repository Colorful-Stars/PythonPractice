#!/usr/bin/env python
# -*- coding = utf-8 -*-

import turtle

def drawtri():
    for i in range(3):
        turtle.seth(i*120)
        turtle.fd(100)
"""
def main():
    turtle.setup(1300, 800, 0, 0)
    turtle.pensize(10)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawtri()

main()
"""
drawtri()