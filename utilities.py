from selenium import webdriver


# Define elements below:
base_url = "https://www.cleartrip.com/"
chrome_driver = r"E:\Dropbox\Udemy-Python\Interview\test_vagrant\libs\chromedriver.exe"
firefox_driver = r"E:\Dropbox\Udemy-Python\Interview\test_vagrant\libs\geckodriver.exe"
ie_driver = r"E:\Dropbox\Udemy-Python\Interview\test_vagrant\libs\IEDriverServer.exe"
user_account_link = "//span[text()='Your trips']"
sign_in_btn = "SignIn"
username = "email"
password = "password"
account_sign_in = "signInButton"
sign_in_error = "There were errors in your submission"
account_sign_in_iframe = "iframe[id='modal_window']"


# Define your utility functions here:
def set_chrome_driver():

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

    return driver


def set_firefox_driver():

    driver = webdriver.Firefox(executable_path=firefox_driver)
    return driver


def set_ie_driver():

    driver = webdriver.Ie(executable_path=ie_driver)
    return driver

