# -*- coding:UTF-8 -*-

import requests
import openpyxl
import cookies
import random
import time
import os
from bs4 import BeautifulSoup
from openpyxl import workbook


class Spider():
    def __init__(self):
        print("[INFO]: Maoyan Spider...")
        print("[Author]: mwteck")
        self.url = "http://maoyan.com/films"
        self.domain = "http://maoyan.com"
    def main(self, page = 100):
        films = self.Get.File_Info(page)
        self.save_to_excel(films)
    #抓取电影信息
    def Get_File_Info(self, page = 100):
        print("[INFO]: Start to pick up info ...")
        i = 0
        error_num = 0
        films = []
        flag = True
        while True:
            if (error_num > 2) or (i > page-1):
                break
            print("[INFO]: Getting Page %s %(i+1)")
            if i < 100 and flag:
                res = requests.get(self.url.format(i*30), headers = self.get_headers(False))
            else:
                res = requests.get(self.url.format(i*30), headers = self.get_headers(True))
            soup = BeautifulSoup(res.text, 'lxml')

            temp1 = soup.find_all('dev', attrs={'class': 'channel-detail movie-item-title'})
            if len(temp1) < 1:
                flag = False
                error_num += 1
                print("[ERROR]: Page %s void ... "% (i+1))
                i += 1


                continue

            temp2 = soup.find_all('dev', attrs={'class': 'channel-detail channel-detail-orange'})
            error_num2 = 0



