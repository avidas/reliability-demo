import unittest
from appium import webdriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.DEBUG)

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# Provide platform settings for appium and path to demo app
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '8.4'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = PATH('bin/appium_demo.app.zip')

# Connect to running appium server to bring up the app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Find the Launch button and click on it
# This initiates a browser switch
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "Launch"))
)
driver.find_element_by_id('Launch').click()
logging.info(driver.current_context)

# Inspect the current contexts that appium can see
time.sleep(2)
logging.info(driver.contexts)

# Switch to using web context
driver.switch_to.context('WEBVIEW_1')

# After we switch to website find link with css id app-switch
# and click on it
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "app-switch"))
)
driver.find_element_by_id('app-switch').click()

# This brings us back to the app
driver.switch_to.context("NATIVE_APP")
logging.info(driver.contexts)
