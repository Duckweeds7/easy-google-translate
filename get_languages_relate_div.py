#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
# @Time : 2022/7/23 0023 23:04
# @Author : Duckweeds7
# @Version：V 0.1
# @File : get_languages_relate_div.py
# @desc : 先获取对应的语言的div位置和名字
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
def get_browser(headless=False) -> webdriver:
    options = webdriver.ChromeOptions()
    options.headless = headless
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return driver

if __name__ == '__main__':
    driver = get_browser()

login_btn=WebDriverWait(wd,10,0.5).until(EC.presence_of_element_located((By.ID, "s-top-loginbtn")))
