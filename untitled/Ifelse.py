#!/usr/bin/env python
# _*_ coding=utf-8 _*_

print "请任意输入一个数字: "
number = int(raw_input())

if number == 10:
    print "您输入的数字是: %d" % number
    print "Right"
elif number > 10:
    print "您输入的数字是: %d" % number
    print "This number is more than 10."
elif number < 10:
    print "您输入的数字是: %d" % number
    print "This number is less than 10."
else:
    print "Wrong"
