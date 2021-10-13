#!/bin/bash/python3
import time
from selenium import webdriver


browser = webdriver.Firefox()
browser.get("https://freebitco.in/?op=home")
time.sleep(10)
