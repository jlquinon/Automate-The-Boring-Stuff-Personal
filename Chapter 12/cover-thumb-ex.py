#! /usr/bin/env python3

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print(f'Found {elem.tag_name} element with that class name!')
except:
    print('Was not able to find an element with that name')
