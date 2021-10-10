#!/usr/bin/env python

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

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


search_bar = browser.find_element_by_id('twotabsearchtextbox')
search_bar.click()
search_bar.send_keys('mackbook')

search_submit = browser.find_element_by_id('nav-search-submit-button')
search_submit.click()

sort_by = browser.find_element_by_class_name('a-dropdown-prompt')
sort_by.click()

sort_selection = browser.find_element_by_link_text('Price: High to Low')
sort_selection.click()

sleep(3) # let results get loaded

search_result = browser.find_element_by_xpath("//div[@data-index='9']//a")
search_result.click()

# if __name__ == "__main__":
    # signIn()