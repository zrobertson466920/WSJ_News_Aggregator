import re
from robobrowser import RoboBrowser
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

# Loading home URL
browser = webdriver.Firefox()
browser.get('http://markets.wsj.com/?mod=Homecle_MDW_MDC')

# Login Credentials
login = browser.find_element_by_link_text("Log In").click()
loginID = browser.find_element_by_id("username").send_keys('zrobertson@uchicago.edu')
loginPass = browser.find_element_by_id("password").send_keys('Alvin1227')
loginReady = browser.find_element_by_class_name("basic-login-submit")
loginReady.submit()

## Close cookie policy if needed
try:
    browser.find_element_by_class_name("close").click()
except NoSuchElementException:
    print('Cookie agreement already acknowledged')

article_count = 0
interest_list = []
## Read in list of companies
interest_list.append('https://quotes.wsj.com/GOGL')

for interest in interest_list:

    browser.get(interest)

    try:
        time_stamp = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(1) + "]/ul/li[1]").text
        headline = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(1) + "]/span/a[1]").text
        link = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(1) + "]/span/a[1]").get_attribute('href')
        article_count += 1
    except NoSuchElementException:

    print("***")
    print(time_stamp)
    print(headline)
    print(link)
    print("***")
