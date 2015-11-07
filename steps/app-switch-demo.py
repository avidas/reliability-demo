from behave import given, when, then
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


@given('we have appium installed')
def step_impl(context):
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '8.4'
    desired_caps['deviceName'] = 'iPhone 6'

    desired_caps['app'] = PATH('../bin/appium_demo.app.zip')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.driver = driver


@when(u'user runs app, clicks on "{button_name}" button in app')
def step_impl(context, button_name):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, button_name))
    )
    context.driver.find_element_by_id('Launch').click()
    logging.info(context.driver.current_context)


@then(u'user clicks on "{button_name}" button in website')
def step_impl(context, button_name):
    time.sleep(3)
    context.driver.switch_to.context('WEBVIEW_1')
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, button_name))
    )
    logging.info(context.driver.contexts)
    time.sleep(3)

    context.driver.find_element_by_id('app-switch').click()


@then(u'it switches back to app')
def step_impl(context):
    time.sleep(3)
    context.driver.switch_to.context("NATIVE_APP")
    logging.info(context.driver.contexts)

    assert context.failed is False
