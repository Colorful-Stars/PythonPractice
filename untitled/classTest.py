#!/usr/bin/env python
# -*- coding = utf-8 -*-

class Student(object):
    def __init__(self, name, score,age):
        self.name = name
        self.score = score
        self.age = age

        #self.__name = name 访问限制

    def print_score(self):
        print("{0} : {1}".format(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def print_age(self):
        print("{}".format(self.age))

bart = Student('Aric', 90, 8)
bart.print_score()
bart.get_grade()
bart.print_age()
