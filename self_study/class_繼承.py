#!/usr/bin//python3
#-*- coding:utf-8 -*-

#父類和子類，子類繼承父類的所有屬性和方法（私有方法除外）

class Ctr(object):
    def run(self):
        print("system starting,")

    def map(self):
        print("chane ")

class Dog(Ctr):
    def run(self):
        print("Dog is running")
    def stop(self):
        print("system stop")

class Cat(Ctr):
    pass

test = Ctr()
test.run()

dog = Dog()
dog.run()
dog.stop()
dog.map()
