# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS()
browser.get('https://www.piaohua.com/html/aiqing/2018/1004/41681.html')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.bot h3')))
print(input)
data = browser.page_source
print data