from creds import *
import helperMethods
import json
import os
import pytest

config_file_path = os.path.abspath("./tests/testCasesConfig.json")
with open(config_file_path, 'r') as f:
    json_dict = json.load(f)

execution_plan = json_dict["execution_plan"]

tc = json_dict['testcase_list']

tc_list = []

execution_range_list = [int(member.strip()) for member in execution_plan.split(',')]
print(execution_range_list)
if len(execution_range_list) % 2 == 0:
    execution_start_list = execution_range_list[0::2]
    # print(execution_start_list)
    execution_end_list = execution_range_list[1::2]
    # print(execution_end_list)
    j = 0
    for i in execution_start_list:
        st = int(i)
        end = int(execution_end_list[j])
        j += 1
        while st <= end:
            tc_list.append(tc[str(st)])
            st += 1
    print(tc_list)
else:
    execution_plan = execution_range_list
    last_execution_start = execution_plan[len(execution_plan) - 1]

    execution_start_list = execution_range_list[0::2]
    # print(execution_start_list)
    execution_end_list = execution_range_list[1::2]
    # print(execution_end_list)
    j = 1
    for i in execution_start_list:
        st = int(i)
        end = int(execution_end_list[j])
        j += 1
        while st <= end:
            tc_list.append(tc[str(st)])
            st += 1
    while last_execution_start <= len(tc):
        tc_list.append(tc[str(last_execution_start)])
        last_execution_start += 1
    print(tc_list)
execution_list = tc_list

def runTC01():
    try:
        helperMethods.startUpApp()
        helperMethods.loginUsingCredentials()
    except Exception as e:
        print(f"Error during TC01: {e}")


def runTC02():
    try:
        helperMethods.closeApp()
    except Exception as e:
        print(f"Error during TC02: {e}")

def runTC03():
    try:
        helperMethods.loadTextTranslationPage()
    except Exception as e:
        print(f"Error during TC03: {e}")

def runTC04():
    try:
        sample_text = 'This is a sample text'
        source_language = 'English' # Must be exact match as in dropdown, can only be empty if using Google Translate
        target_language = 'Arabic' # Must be exact match as in dropdown
        translation_service = 'Google' # Must be exactly 'Microsoft' or 'Google'
        helperMethods.textTranslationTest(sample_text, source_language, target_language,translation_service)
        
    except Exception as e:
        print(f"Error during TC04: {e}")

for i in execution_list:
    if (i == 'TC_01_Open_And_Login_Application'):
        runTC01()
    if (i == 'TC_02_Logout_And_Close_Application'):
        runTC02()
    if (i == 'TC_03_Load_Text_Translation_Page'):
        runTC03()
    if (i == 'TC_04_Google_Text_Translation_English_Arabic'):
        runTC04()
# runTC01()
# runTC03()
# runTC04()
