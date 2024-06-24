from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Protocol, Optional
from abc import ABC
from creds import *

# driver = webdriver.Chrome()
# time.sleep(10)

chrome_options = webdriver.ChromeOptions()

# Keeps browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options)
driver.get("https://translation-dev.amgen.com/file-translation")
print(driver.title)

time.sleep(30) # wait for popup to time out and proceed w/ log in

USERNAME = AUTH_OKTA_USERNAME # imported from creds file
PASSWORD = AUTH_OKTA_PASSWORD # imported from creds file

username_field_xpath = '//*[@id="input28"]'
username_field = driver.find_element(By.XPATH, username_field_xpath)
username_field.send_keys(USERNAME)


next_button_xpath = '//*[@id="form20"]/div[2]/input'
next_button = driver.find_element(By.XPATH, next_button_xpath)
next_button.click()

time.sleep(5)

password_field_xpath = '//*[@id="input60"]'
password_field = driver.find_element(By.XPATH, password_field_xpath)
password_field.send_keys(PASSWORD)

verify_button_xpath = '//*[@id="form52"]/div[2]/input'
verify_button = driver.find_element(By.XPATH, verify_button_xpath)
verify_button.click()