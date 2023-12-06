from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains

import time

# Тест на натискання на кнопку:
def test_01():
    driver = Chrome()
    driver.get('https://tshina.ua')
    search_field_locator = '/html/body/main/div[2]/div/div[1]/div/a[1]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys(Keys.ENTER)

    time.sleep(5)

def test_02():
    driver = Chrome()
    driver.get('https://tshina.ua')
    search_field_locator = '/html/body/main/div[2]/div/div[1]/div/a[1]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    search_filter_button= '/ html / body / main / div[5] / div / button'
    element_filter = driver.find_element(by='xpath', value=search_filter_button)
    element_filter.send_keys(Keys.ENTER)
    time.sleep(5)
    checkbox_adata_locator = '//*[@id="tire-filter"]/div[2]/form/div/div[4]/div[2]/div[1]/div[2]/label[1]/span'
    checkbox_adata = driver.find_element('xpath', checkbox_adata_locator)
    checkbox_adata.click()
    time.sleep(5)

def test_03():
    driver = Chrome()
    driver.get('https://www.ukr.net/')
    search_field_input = '//*[@id="search-input"]'
    element = driver.find_element(by='xpath', value=search_field_input)
    element.send_keys('погода київ')
    element.send_keys(Keys.ENTER)
    time.sleep(5)

def test_04():
    driver = Chrome()
    driver.get('https://www.ukr.net/')
    search_field_input = '//*[@id="search-input"]'
    element = driver.find_element(by='xpath', value=search_field_input)
    element.send_keys('футбот')
    element.send_keys(Keys.ENTER)
    search_second_page =  '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[2]/div/div[2]'
    second_element = driver.find_element(by='xpath', value=search_second_page)
    second_element.click()

    time.sleep(5)

def test_05():
    driver = Chrome()
    driver.get('https://tshina.ua')
    search_field_locator = '/html/body/main/div[2]/div/div[1]/div/a[1]'
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    search_filter_button= '/ html / body / main / div[5] / div / button'
    element_filter = driver.find_element(by='xpath', value=search_filter_button)
    element_filter.send_keys(Keys.ENTER)
    time.sleep(5)
    checkbox_adata_locator = '//*[@id="tire-filter"]/div[2]/form/div/div[4]/div[2]/div[1]/div[2]/label[2]/span'
    checkbox_adata = driver.find_element('xpath', checkbox_adata_locator)
    checkbox_adata.click()
    time.sleep(5)
    search_set_filter = '//*[@id="set_filter"]'
    element_set_filter = driver.find_element(by='xpath', value=search_set_filter)
    element_set_filter.click()
    time.sleep(5)
    search_selector = '/html/body/main/div[6]/div[2]/div/div[1]/div[2]/div/div/p'
    element_selector = driver.find_element(by='xpath', value=search_selector)
    element_selector.click()
    time.sleep(5)
    search_min = '/html/body/main/div[6]/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/label'
    element_selector_min = driver.find_element(by='xpath', value=search_min)
    element_selector_min.click()
    time.sleep(5)
