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
import csv

def main():

    # Get file and reference info
    filename = input("What companies are we looking at? (cv) \n")
    date = input("How far back should we look to? (m/d/y) \n")
    dt = datetime.datetime.strptime(date, "%m/%d/%y")

    # Build interst interest_list
    interest_list = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        next(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            words = row[0].split()
            row[0] = words[0]
            interest_list.append(row)

    csvfile.close()

    #  printing first 5 rows
    print("The companies: \n")
    for row in interest_list:
        # parsing each column of a row
        print(row[0] + ": " + row[1])
    print("The number of companies is: " + str(len(interest_list)))

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

    for interest in interest_list:

        interest_url = "https://quotes.wsj.com/" + interest[0]

        browser.get(interest_url)

        for counter in range(1,4):
            try:
                time_stamp = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(counter) + "]/ul/li[1]").text
                headline = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(counter) + "]/span/a[1]").text
                link = browser.find_element_by_xpath("//ul[@id='newsSummary_c']/li[" + str(counter) + "]/span/a[1]").get_attribute('href')
                article_count += 1
            except NoSuchElementException:
                break

            try:
                ts = datetime.datetime.strptime(time_stamp, "%m/%d/%y")
            except ValueError:
                print(interest[0] + ": " + time_stamp)
                print(headline)
                print(link + '\n')

            if dt <= ts:
                print(interest[0] + ": " + time_stamp)
                print(headline)
                print(link + '\n')
            else:
                break

main()
