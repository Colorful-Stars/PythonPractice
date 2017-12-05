#!/usr/bin/env python
# _*_ coding=utf-8 _*_

__metaclass__ = type

class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def color(self, color):
        print "%s is %s" % (self.name, color)

girl = Person('Canglaoshi')
name = girl.getName()
print "the person's name is: ", name
girl.color("white")
print "------"
print girl.name

