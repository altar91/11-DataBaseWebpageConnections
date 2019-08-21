import requests
import warnings
warnings.filterwarnings("ignore")
import sys
import os
import win32com.client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#Install geckodriver first

if __name__ == '__main__':
    try:

        browser = webdriver.Firefox()
        browser.get("https://web_page_url")
        xpath_User_Name = '/html/body/font/table/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[2]/input' #copy xpath
        xpath_User_Password = '/html/body/font/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/input' #copy xpath
        xpath_Login_Button = '/html/body/font/table/tbody/tr/td[2]/form/table[3]/tbody/tr[1]/td[1]/input' #copy xpath
        box = browser.find_element_by_xpath(xpath_User_Name)
        box.send_keys('user_name')
        box2 = browser.find_element_by_xpath(xpath_User_Password)
        box2.send_keys('password')

        #if you want to wait page to load use this line
        #myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, xpath_Login_Button)))
        btn = browser.find_element_by_xpath(xpath_Login_Button)
        btn.click()

    finally:

        browser.quit()
