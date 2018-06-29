from selenium import webdriver
from utilities import *
import time


def sign_in_test():

    driver = set_chrome_driver()
    driver.maximize_window()
    driver.get(url=base_url)
    time.sleep(5)
    driver.find_element_by_xpath(user_account_link).click()
    driver.find_element_by_id(sign_in_btn).click()
    time.sleep(5)

    driver.switch_to_frame(driver.find_element_by_css_selector(account_sign_in_iframe))
    driver.find_element_by_id(username).send_keys("testuser")
    driver.find_element_by_id(password).send_keys("secret")
    driver.find_element_by_id(account_sign_in)
    time.sleep(5)
    if sign_in_error in driver.page_source:
        print("Cannot login, give correct userid/password..")
    else:
        print("Success")

sign_in_test()