############################### IMPORT LIBS/PCKGS ###############################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from creds import *
import tests
# import klembord

############################### SET UP ###############################

# Variable to store custom settings for browser
chrome_options = webdriver.ChromeOptions()

# Adds custom setting to keep browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options) # Stores options into web driver

def startUpApp():

    driver.get("https://translation-dev.amgen.com/file-translation") # Opens AI Translation app FT page - allows script to access buttons on top

    #time.sleep(10) # wait for popup to time out and log in page to load -> now handled by login function

############################### LOG IN ###############################

USERNAME = AUTH_OKTA_USERNAME # imported from creds file
PASSWORD = AUTH_OKTA_PASSWORD # imported from creds file

def loginUsingCredentials():
    try:
        # waits for username login to load
        user_login_xpath = '//*[@id="form20"]/div[1]/div[3]/div[1]/div[1]'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, user_login_xpath)))

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

        # Waits for a specific element that indicates the login was successful and the page has fully loaded
        # post_login_element_xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]'  # Example element -> 'View the FAQs'
        # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, post_login_element_xpath)))
    
    except Exception as e:
        print(f"Error during login: {e}")

############################### TESTING ###############################

def textTranslationTest(): # Can't test right now -> issue with login (continuously loading after login)
    
    def googleTextTranslateTest():

        # Finds translation service box and clicks dropdown button to initiate typing in service
        translation_service_dropdown_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[2]/div[1]/div/div/div[2]/div'
        translation_service_dropdown_button = driver.find_element(By.XPATH, translation_service_dropdown_button_xpath)
        translation_service_dropdown_button.click()

        # Finds translation service input box and enters in desired service
        translation_service_select_xpath = '//*[@id="react-select-5-input"]'
        translation_service_select = driver.find_element(By.XPATH, translation_service_select_xpath)
        translation_service_select.send_keys(tests.textTranslationTestCases.translation_service)
        translation_service_select.send_keys(Keys.ENTER)

        # Checks if the source language variable is empty (happens user wants source language to be auto detected)
        if (tests.textTranslationTestCases.source_language_1 != ''):

            # Finds the 'Source Language' box and clicks the dropdown button to initiate typing in language
            source_language_dropdown_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[1]/div[1]/div[2]/div/div[2]/div'
            source_language_dropdown_button = driver.find_element(By.XPATH, source_language_dropdown_button_xpath)
            source_language_dropdown_button.click()
        
            # Find source language input box and type in source language
            source_language_select_xpath = '//*[@id="react-select-6-input"]'
            source_language_select = driver.find_element(By.XPATH, source_language_select_xpath)
            source_language_select.send_keys(tests.textTranslationTestCases.source_language_1)
            source_language_select.send_keys(Keys.ENTER)
        else:
            print("Auto detecting language")

        # Find target language input box and type in target language
        target_language_select_xpath = '//*[@id="react-select-7-input"]'
        target_language_select = driver.find_element(By.XPATH, target_language_select_xpath)
        target_language_select.send_keys(tests.textTranslationTestCases.target_language_1)
        target_language_select.send_keys(Keys.ENTER)

        # Finds source text box and enters in sample text
        source_text_box_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[2]/div[1]/label/div/textarea'
        source_text_box = driver.find_element(By.XPATH, source_text_box_xpath)
        source_text_box.click()
        source_text_box.send_keys(tests.textTranslationTestCases.sample_text_1)

        # Finds 'Translate' button and clicks it
        translate_text_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[4]/button'
        translate_text_button = driver.find_element(By.XPATH, translate_text_button_xpath)
        translate_text_button.click()

        # Finds translated text and stores it in variable
        translated_text_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[2]/div[2]/label/div/textarea'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, translated_text_xpath)))

        translated_text = driver.find_element(By.XPATH, translated_text_xpath).text
        print(translated_text)


        ### Add History tab test  - make sure to everything below for Microsoft ####

        # Clicks on History tab
        history_text_translation_tab_xpath = '//*[@id="uncontrolled-tab-example-tab-file-upload-log"]'
        history_text_translation_tab = driver.find_element(By.XPATH, history_text_translation_tab_xpath)
        history_text_translation_tab.click()

        # Waits for page to load by looking for "Original Text" and then clicks on refresh button
        original_text_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload-log"]/div/section/div[2]/div/div/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[1]'
        refresh_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload-log"]/div/section/div[1]/div/div/div/button'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, original_text_xpath)))

        refresh_button = driver.find_element(By.XPATH, refresh_button_xpath)
        refresh_button.click()

        # Searches for sample text that was translated in history tab
        sample_text_translation_search_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload-log"]/div/section/div[1]/div/div/div/span/span/span[1]/input'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, original_text_xpath)))

        sample_text_translation_search = driver.find_element(By.XPATH, sample_text_translation_search_xpath)
        sample_text_translation_search.send_keys(tests.textTranslationTestCases.sample_text_1)
        sample_text_translation_search.send_keys(Keys.ENTER)

        # Preview translation of sample text (selectin top row) - NEED TO FIX
        preview_text_translation_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload-log"]/div/section/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[7]/div/div/div/svg[1]'
        preview_text_translation = driver.find_element(By.XPATH, preview_text_translation_xpath)
        preview_text_translation.click()

        # # Download translated text - uncomment and test after preview button is fixed
        # download_translated_text_button_xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[1]/button'
        # download_translated_text_button = driver.find_element(By.XPATH, download_translated_text_button_xpath)
        # download_translated_text_button.click()

    def microsoftTextTranslateTest():

        # Finds translation service box and clicks dropdown button to initiate typing in service
        translation_service_dropdown_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[2]/div[1]/div/div/div[2]/div'
        translation_service_dropdown_button = driver.find_element(By.XPATH, translation_service_dropdown_button_xpath)
        translation_service_dropdown_button.click()

        # Finds translation service input box and enters in desired service
        translation_service_select_xpath = '//*[@id="react-select-5-input"]'
        translation_service_select = driver.find_element(By.XPATH, translation_service_select_xpath)
        translation_service_select.send_keys(tests.textTranslationTestCases.translation_service)
        translation_service_select.send_keys(Keys.ENTER)

        ### NOTE_to_remember: Microsoft does not offer auto translate, thus the if statement will not be here

        # Finds the 'Source Language' box and clicks the dropdown button to initiate typing in language
        source_language_dropdown_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[1]/div[1]/div[2]/div/div[2]/div'
        source_language_dropdown_button = driver.find_element(By.XPATH, source_language_dropdown_button_xpath)
        source_language_dropdown_button.click()
    
        # Find source language input pox and type in source language
        source_language_select_xpath = '//*[@id="react-select-6-input"]'
        source_language_select = driver.find_element(By.XPATH, source_language_select_xpath)
        source_language_select.send_keys(tests.textTranslationTestCases.source_language_1)
        source_language_select.send_keys(Keys.ENTER)

        # Find target language input box and type in target language
        target_language_select_xpath = '//*[@id="react-select-7-input"]'
        target_language_select = driver.find_element(By.XPATH, target_language_select_xpath)
        target_language_select.send_keys(tests.textTranslationTestCases.target_language_1)
        target_language_select.send_keys(Keys.ENTER)

        # Finds source text box and enters in sample text
        source_text_box_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[2]/div[1]/label/div/textarea'
        source_text_box = driver.find_element(By.XPATH, source_text_box_xpath)
        source_text_box.click()
        source_text_box.send_keys(tests.textTranslationTestCases.sample_text_1)

        # Finds 'Translate' button and clicks it
        translate_text_button_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[4]/button'
        translate_text_button = driver.find_element(By.XPATH, translate_text_button_xpath)
        translate_text_button.click()

        # Finds translated text and stores it in variable
        translated_text_xpath = '//*[@id="uncontrolled-tab-example-tabpane-file-upload"]/div/div[3]/div[2]/div[2]/label/div/textarea'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, translated_text_xpath)))

        translated_text = driver.find_element(By.XPATH, translated_text_xpath).text
        print(translated_text)
    
    try:
        # Finds 'Text' button and clicks on it, taking it to the Text Translation page
        text_translation_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[2]/a'
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, text_translation_page_button_xpath)))
        text_translation_page_button = driver.find_element(By.XPATH, text_translation_page_button_xpath)
        text_translation_page_button.click()

        if (tests.textTranslationTestCases == 'Google Translate'):
            googleTextTranslateTest()
        elif (tests.textTranslationTestCases == 'Microsoft Translator'):
            microsoftTextTranslateTest()
        else:
            # Default selection will be google translate
            googleTextTranslateTest()


    #### NEED TO INCLUDE BUSINESS GLOSSARY TESTING ####

    except Exception as e:
        print(f"Error during text translation test: {e}")

def fileTranslationTest():
    try:
        # Finds 'File' button and clicks on it, taking it to the File Translation page 
        file_translation_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[1]/a'
        file_translation_page_button = driver.find_element(By.XPATH, file_translation_page_button_xpath)
        file_translation_page_button.click()

        ### INCOMPLETE - need to have dev fixed ###
    except Exception as e:
        print(f"Error during file translation test: {e}")

def businessGlossaryTest():
    try:
        # Finds 'Business Glossary' button and clicks on it, taking it to the Business Glossary page
        business_glossary_page_button_xpage = '//*[@id="navbarNav"]/ul[1]/li[3]/a'
        business_glossary_page_button = driver.find_element(By.XPATH, business_glossary_page_button_xpage)
        business_glossary_page_button.click()

        ### INCOMPLETE - need to have dev fixed ###
    except Exception as e:
        print(f"Error during business glossary test: {e}")

def faqTest():
    try:
        # Finds 'FAQ' button and clicks on it, taking to the FAQ page
        faq_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[4]/a'
        faq_page_button = driver.find_element(By.XPATH, faq_page_button_xpath)
        faq_page_button.click()

        ### INCOMPLETE - need to have dev fixed ###
    except Exception as e:
        print(f"Error during FAQ test: {e}")

def usageMetricsTest():
    try:
        # Finds 'Usage Metrics' button and clicks on it, taking to the Usage Metrics page
        usage_metrics_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[5]/a'
        usage_metrics_page_button = driver.find_element(By.XPATH, usage_metrics_page_button_xpath)
        usage_metrics_page_button.click()

        ### INCOMPLETE - need to have dev fixed ###
    except Exception as e:
        print(f"Error during usage metrics test: {e}")

def adminTest():
    try:
        # Finds 'Admin' button and clicks on it, taking to the Admin page
        admin_page_button_xpath = '//*[@id="navbarNav"]/ul[1]/li[6]/a'
        admin_page_button = driver.find_element(By.XPATH, admin_page_button_xpath)
        admin_page_button.click()

        ### INCOMPLETE - need to have dev fixed ###

    except Exception as e:
        print(f"Error during admin test: {e}")

def landingTest():
    try:
        landing_page_button_xpath = '//*[@id="root"]/div/div/header/nav/div/a'
        landing_page_button = driver.find_element(By.XPATH, landing_page_button_xpath)
        landing_page_button.click()

        ### INCOMPLETE

    except Exception as e:
        print(f"Error during landing page test: {e}")

# # Call methods
startUpApp() # fully functional
loginUsingCredentials() # fully functional

# # Uncomment to test other functions after fixing the login issue

textTranslationTest()
# fileTranslationTest()
# businessGlossaryTest()
# faqTest()
# usageMetricsTest()
# adminTest()
# landingTest()