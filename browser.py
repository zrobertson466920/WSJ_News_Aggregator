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

# Loading home URL
browser = webdriver.Firefox()
browser.get('http://markets.wsj.com/?mod=Homecle_MDW_MDC')

# Login Credentials
login = browser.find_element_by_link_text("Log In").click()
loginID = browser.find_element_by_id("username").send_keys('zrobertson@uchicago.edu')
loginPass = browser.find_element_by_id("password").send_keys('Alvin1227')
loginReady = browser.find_element_by_class_name("basic-login-submit")
loginReady.submit()

browser.get('https://quotes.wsj.com/GOGL')

## Close cookie policy if needed
try:
    browser.find_element_by_class_name("close").click()
except NoSuchElementException:
    print('Cookie agreement already acknowledged')

Articles = {}
Unigrams = {}
article_count = 0
df = []
df.append('https://quotes.wsj.com/GOGL')

for i in df:

    # Get headlines
    h_bool = 1

    try:
        headline = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[1]/ul/li[1]").text
    except NoSuchElementException:
        h_bool = 0

    # Enter article headline into dictionary
    Articles[headline] = {}

    print(headline)

    article_count += 1
