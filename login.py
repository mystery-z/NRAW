from selenium import webdriver
import time, urllib.request
import requests
import os
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys


def login(username, password):
		

	options = FirefoxOptions()
	options.add_argument("--headless")
	
	driver = webdriver.Firefox(options=options)

	driver.get("https://www.reddit.com/login/")

	driver.find_element(By.ID, "loginUsername").send_keys(username)
	driver.find_element(By.ID, "loginPassword").send_keys(password)
	driver.find_element(By.ID, "loginPassword").send_keys(Keys.RETURN)
