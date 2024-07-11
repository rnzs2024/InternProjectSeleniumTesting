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

if ('TC_01_Open_And_Login_Application' in execution_list):
    runTC01()
if ('TC_02_Logout_And_Close_Application' in execution_list):
    runTC02()
