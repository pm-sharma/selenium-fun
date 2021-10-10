#!/usr/bin/env python

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

browser.save_screenshot("/home/kush/Desktop/github/selenium-fun/ubuntu_setup/images/items_search.png")

sleep(1)
sort_selection = browser.find_element_by_link_text('Price: High to Low')
sort_selection.click()

sleep(3) # let results get loaded

# click on item
search_result = browser.find_element_by_xpath("//div[@data-index='9']//a")
search_result.click()

sleep(3)

# switch to window 2
browser.switch_to.window(browser.window_handles[-1]) # use 0 for main tab, this is for last opened tab
wishlist_button = browser.find_element_by_id('add-to-wishlist-button-submit')
wishlist_button.click()

sleep(1)

html = browser.find_element_by_tag_name('html')
for _ in range(3):
    html.send_keys(Keys.END)
    sleep(1)

view_wishlist = browser.find_element_by_link_text('View Wish List')
view_wishlist.click()

sleep(2)

# SignOut
action = ActionChains(browser)
first_level_menu = browser.find_element_by_id('nav-link-accountList-nav-line-1')
action.move_to_element(first_level_menu).perform()
second_level_menu = browser.find_element_by_xpath('//*[@id="nav-item-signout"]/span')
action.move_to_element(second_level_menu).perform()
second_level_menu.click()

browser.quit() # close

# if __name__ == "__main__":
    # signIn()