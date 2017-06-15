#!/usr/bin/env python

__author__ = "Sam McCaffrey"
__copyright__ = "Copyright 2017, Sam McCaffrey"
__license__ = "Apache-2.0"
__version__ = "1.0.1"
__maintainer__ = "Sam McCaffrey"
__email__ = "samccaff@asu.edu"
__status__ = "Production"

import selenium
import getpass
import time
import logging
import pandas as pd
from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assignmentSelector(driver, test, module, **kwargs):
    try:
        driver.find_element_by_xpath('//a[@title=' + "\"" + test + " item options" + "\"" ']').click()
        logging.info('\t' + test + '\t\t\t\tPASSED')
    except Exception as e:
        logging.info('\t' + test + '\t\t\t\tFAILED')
        print("Error with " + module + " : " + test + "...skipping")
        pass

def edit_test_options(driver, **kwargs):
    try:
        driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
    except Exception as e:
        pass

def start_restrict(driver, state, **kwargs):
    try:
        if state:
           driver.find_element_by_id('start_restrict').click()
        else:
           pass
    except Exception as e:
        pass

def is_checked(self, driver, item, **kwargs):
  checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
  return checked

def end_restrict(driver, state, **kwargs):
    try:
        if state:
            driver.find_element_by_id('end_restrict').clear()
            driver.find_element_by_id('end_restrict').click()
        else:
            driver.find_element_by_id('end_restrict').clear()
    except Exception as e:
        pass

def _dueDate(driver, state, **kwargs):
    try:
        if state:
            #element = driver.find_element_by_name('due_date_in_use')
            driver.find_element_by_id('_dueDate').click()
    except Exception as e:
        pass

def _lateSubmission(driver, state, **kwargs):
    try:
        if state:
            driver.find_element_by_id('doNotAllowLateSubmission').click()
            #while str(driver.execute_script("return document.getElementById('doNotAllowLateSubmission').checked")) == 'False':
            #    element = driver.find_element_by_name('doNotAllowLateSubmission')
            #    element.click()
        else:
            pass
    except Exception as e:
        pass

def dp_dueDate_date(driver, date, **kwargs):
    try:
        driver.find_element_by_id('dp_dueDate_date').clear()
        driver.find_element_by_id('dp_dueDate_date').send_keys(date)
    except Exception as e:
        pass

def tp_dueDate_time(driver, time, **kwargs):
    try:
        driver.find_element_by_id('tp_dueDate_time').clear()
        driver.find_element_by_id('tp_dueDate_time').send_keys(time)
    except Exception as e:
        pass

def cancel(driver, **kwargs):
    try:
        driver.find_element_by_name('bottom_Cancel').click()
    except Exception as e:
        pass

def submit(driver, **kwargs):
    try:
        driver.find_element_by_name('bottom_submit').click()
    except Exception as e:
        pass
def errorHandler1():
    return