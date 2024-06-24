############################### IMPORT LIBS/PCKGS ###############################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from creds import *
import tests

############################### SET UP ###############################

# Variable to store custom settings for browser
chrome_options = webdriver.ChromeOptions()

# Adds custom setting to keep browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options) # Stores options into web driver

def startUpApp():

    driver.get("https://translation-dev.amgen.com/file-translation") # Opens AI Translation app

    time.sleep(30) # wait for popup to time out and log in page to load

############################### LOG IN ###############################


USERNAME = AUTH_OKTA_USERNAME # imported from creds file
PASSWORD = AUTH_OKTA_PASSWORD # imported from creds file

def loginUsingCredentials():

    # Finds the username box through XPATH and inputs username variable
    username_field_xpath = '//*[@id="input28"]'
    username_field = driver.find_element(By.XPATH, username_field_xpath)
    username_field.send_keys(USERNAME)

    # Clicks 'Next' button to submit username
    next_button_xpath = '//*[@id="form20"]/div[2]/input'
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    next_button.click()

    time.sleep(5) # Buffer to let page load

    # Finds the passwrd box through XPATH and inputs password variable
    password_field_xpath = '//*[@id="input60"]'
    password_field = driver.find_element(By.XPATH, password_field_xpath)
    password_field.send_keys(PASSWORD)

    # Clicks 'Verify' button to submit password and login
    verify_button_xpath = '//*[@id="form52"]/div[2]/input'
    verify_button = driver.find_element(By.XPATH, verify_button_xpath)
    verify_button.click()

############################### TESTING ###############################

def textTranslationTest(): # Can't test right now -> issue with login (continuously loading after login)
    
    # Finds 'Text' button and clicks on it, taking it to the Text Translation page
    text_translation_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[2]/a'
    text_translation_page_button = driver.find_element(By.XPATH, text_translation_page_button_xpath)
    text_translation_page_button.click()

    # Finds the 'Source Text' box to enter in text to be translated
    source_text_box_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[2]/div[1]/label/div/textarea'
    source_text_box = driver.find_element(By.XPATH, source_text_box_xpath)
    source_text_box.send_keys(tests.textTranslationTestCases.sample_text_1)


    ### INCOMPLETE - need to have dev fixed ###

def fileTranslationTest():

    # Finds 'File' button and clicks on it, taking it to the File Translation page 
    file_translation_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[1]/a'
    file_translation_page_button = driver.find_element(By.XPATH, file_translation_page_button_xpath)
    file_translation_page_button.click()

    ### INCOMPLETE - need to have dev fixed ###

def businessGlossaryTest():

    # Finds 'Business Glossary' button and clicks on it, taking it to the Business Glossary page
    business_glossary_page_button_xpage = '//*[@id="navbarNav"]/ul[1]/li[3]/a'
    business_glossary_page_button = driver.find_element(By.XPATH, business_glossary_page_button_xpage)
    business_glossary_page_button.click()

    ### INCOMPLETE - need to have dev fixed ###

def faqTest():

    # Finds 'FAQ' button and clicks on it, taking to the FAQ page
    faq_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[4]/a'
    faq_page_button = driver.find_element(By.XPATH, faq_page_button_xpath)
    faq_page_button.click()

    ### INCOMPLETE - need to have dev fixed ###

def usageMetricsTest():

    # Finds 'Usage Metrics' button and clicks on it, taking to the Usage Metrics page
    usage_metrics_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[5]/a'
    usage_metrics_page_button = driver.find_element(By.XPATH, usage_metrics_page_button_xpath)
    usage_metrics_page_button.click()

    ### INCOMPLETE - need to have dev fixed ###

def adminTest():

    # Finds 'Admin' button and clicks on it, taking to the Admin page
    admin_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[6]/a'
    admin_page_button = driver.find_element(By.XPATH, admin_page_button_xpath)
    admin_page_button.click()

    ### INCOMPLETE - need to have dev fixed ###

# # Call methods
# startUpApp() # fully functional
# loginUsingCredentials() # fully functional
# textTranslationTest()
# fileTranslationTest()
# businessGlossaryTest()
# faqTest()
# usageMetricsTest()
# adminTest()