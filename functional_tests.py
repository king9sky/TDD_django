#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Marvin King
# Date     : 2019-01-31 
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title