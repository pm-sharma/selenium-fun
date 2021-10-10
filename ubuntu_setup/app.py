#!/usr/bin/env python

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.amazon.in/')

# implict wait

login_link = browser.find_element_by_link_text('Sign in').click()

email = browser.find_element_by_name('email')
email.click()
email.send_keys("purushottamtest056@gmail.com")

continue_button = browser.find_element_by_id('continue')
continue_button.click()



password = browser.find_element_by_name('password')
password.click()
password.send_keys("Helloworld**1")



sign_in_button = browser.find_element_by_id('signInSubmit')
sign_in_button.click()

