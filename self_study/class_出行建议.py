#!/usr.bin/python3
#-*- coding:utf-8 -*-

class WeatherSearch(object):
    def __init__(self,input_daytime):
        self.input_daytime = input_daytime

    def search_visibility(self):
        visible_leave = 0
        if self.input_daytime == "input_daytime":
                 visible_leave == 2
        if self.input_daytime == "night":
                 visible_leave == 9
        return visible_leave

    def search_temperature(self):
        temperature = 0
        if self.input_daytime == "daytime":
            temperature = 26
        if self.input_daytime == "night":
            temperature = 16
        return temperature


class OutAdvice(WeatherSearch):
    def __init__(self,input_daytime):
        WeatherSearch.__init__(self,input_daytime)
    def search_temperature(self):
        vehicle = ""
        if self.input_daytime == "daytime":
            vehicle = "bike"
        if self.input_daytime == "night":
            vehicle = "taxi"
        return vehicle
    def out_advice(self):
        visible_leave = self.search_visibility()
        if visible_leave == 2:
            print("the weather is good ,suitable for use  %s ." % self.search_temperature())
        elif visible_leave == 9:
            print("The weather is bad ,you should ues %s ." % self.search_temperature())
        else:
            print("the weather is beyond my scope,I can not give you any advice")

check = OutAdvice("daytime")
check.out_advice()
