#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
# @Time : 2022/7/23 0023 0:56
# @Author : Duckweeds7
# @Version：V 0.1
# @File : easy_google_translate.py
# @desc :
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://translate.google.com/?hl=en&sl={}&tl={}&text={}&op=translate"
DEFAULT_LANGUAGES = {"en": ""}


def get_browser(headless=False) -> webdriver:
    options = webdriver.ChromeOptions()
    options.headless = headless
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return driver


def translate(text):
    if type(text) == dict:
        translate_by_dict(text)
    return


def translate_by_dict(_dict):
    driver = None
    for k in _dict.keys():
        sl = _dict[k].get("sl", "auto") or "auto"
        tl = _dict[k].get("tl", {}) or DEFAULT_LANGUAGES
        text = _dict[k].get("value")
        for l in tl.keys():
            if not driver:
                driver = get_browser()
                driver.get(BASE_URL.format(sl, l, text))
            else:
                driver.find_element_by_class_name("VfPpkd-Bz112c-RLmnJb").click()  # 点击目标语言下拉框
                driver.find_elements_by_xpath(
                    '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div/div[2]') # 点击第一个语言
            translated_value = None
            while not translated_value or "..." in translated_value:
                translated_value = driver.find_element_by_class_name("J0lOec").text
                time.sleep(1)
            tl[l] = translated_value
            pass


if __name__ == '__main__':
    translate_dict = {
        "title": {
            "value": "次韵董景先",
            "sl": "zh-CN",
            "tl": {"en": ""}
        },
        "author": {
            "value": "韩淲",
            "sl": "zh-CN",
            "tl": {"en": ""}
        },
        "content": {
            "value": "冰玉胸怀隔几尘，下帷犹复擅诗声。人间是处堪娱意，南北两山湖水清。",
            "sl": "zh-CN",
            "tl": {"en": ""}
        }
    }
    translate(translate_dict)
