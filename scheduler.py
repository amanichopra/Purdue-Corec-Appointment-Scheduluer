#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import argparse

parser = argparse.ArgumentParser(description='credentials')
parser.add_argument('--username')
parser.add_argument('--password')
parser.add_argument('--tries', type=int, default=4)
parser.add_argument('--pathToChromedriver')
parser.add_argument('--d', default=None)
parser.add_argument('--timeSlot')
args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument('--incognito')
if args.d: chrome_options.add_argument(args.d)
chrome_options.add_argument("--window-size=1792,1120") # ensure this matches your screen resolution

driver = webdriver.Chrome(args.pathToChromedriver,options=chrome_options)
for i in range(args.tries):
    driver.get(
        'https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwww.purdue.edu%2Fapps%2Fidphs%2FAuthn%2FExtCas%3Fconversation%3De1s1&entityId=https%3A%2F%2Frecwell.purdue.edu%2Fshibboleth')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys(args.username)
    driver.find_element_by_id('password').send_keys(args.password)
    driver.find_element_by_css_selector(
        '#boilerKeyLogoAndSubmit > div.submit > input[type=submit]:nth-child(4)').click()

    try:
        driver.find_element_by_id('status')
        continue
    except NoSuchElementException:
        pass

    driver.get('https://recwell.purdue.edu/booking')
    time.sleep(2)
    driver.find_element_by_css_selector('#loginLink').click()
    time.sleep(2)
    driver.find_element_by_css_selector('#divLoginOptions > div.modal-body > div:nth-child(3) > div > button').click()
    time.sleep(2)
    driver.find_element_by_css_selector('#divBookingProducts-large > div:nth-child(1) > a > div').click()
    time.sleep(2)
    driver.find_element_by_css_selector(
        '#divBookingDateSelector > div.visible-lg.visible-md.hidden-sm.hidden-xs > div.flex-center.margin-top-24 > button:nth-child(2)').click()
    time.sleep(2)
    for i in range(20):
        try:
            if driver.find_element_by_css_selector(
                    '#divBookingSlots > div > div:nth-child({}) > p > strong'.format(i)).text.startswith(args.timeSlot):
                try:
                    time.sleep(3)
                    driver.find_element_by_css_selector(
                        '#divBookingSlots > div > div:nth-child({}) > div > button'.format(i)).click()
                except NoSuchElementException:
                    pass
                except ElementClickInterceptedException:
                    print('issue')
                    pass
                break
        except NoSuchElementException:
            pass
    break
driver.quit()