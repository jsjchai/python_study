# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def url_get():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url='https://www.baidu.com/')
    wb_name = browser.find_element_by_id("kw")
    print(wb_name)
    wb_name.send_keys(input('输入搜索内容：'))
    sleep(1)
    search = browser.find_element_by_id('su')
    search.click()
    sleep(1)
    bz_num = browser.find_element_by_id("content_left").find_elements_by_xpath("//h3[@class='t']")
    for title in bz_num:
      print(title.text)


if __name__ == '__main__':
    url_get()




