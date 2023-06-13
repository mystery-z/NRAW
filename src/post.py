import time, urllib.request
import requests
import os
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver



def post(username, password, sub, title, content_type, content):

	options = FirefoxOptions()
	options.add_argument("--headless")
	
	driver = webdriver.Firefox(options=options)

	driver.get("https://www.reddit.com/login/")

	driver.find_element(By.ID, "loginUsername").send_keys(username)
	driver.find_element(By.ID, "loginPassword").send_keys(password)
	driver.find_element(By.ID, "loginPassword").send_keys(Keys.RETURN)

	time.sleep(10) ### can change this buffer time if internet speeds are faster

	driver.get("https://www.reddit.com/submit/")
	driver.find_element(By.CLASS_NAME, "_1MHSX9NVr4C2QxH2dMcg4M").send_keys(sub)
	driver.find_element(By.CLASS_NAME, "_1MHSX9NVr4C2QxH2dMcg4M").send_keys(Keys.RETURN)
	driver.find_element(By.CLASS_NAME, "PqYQ3WC15KaceZuKcFI02").send_keys(title)
	
	if content_type == "post":
		driver.find_element(By.CLASS_NAME, "PqYQ3WC15KaceZuKcFI02").send_keys(Keys.TAB)
		driver.find_element(By.CLASS_NAME, "notranslate").send_keys(content)
	elif content_type == "imagevideo":
		print("working on this...")
	elif content_type == "link":
		driver.find_element(By.XPATH, "//div[@class='_3fd4Ceu6mb8NI6WVk0Yv5c']/button[3]").click()
		driver.find_element(By.CLASS_NAME, "PqYQ3WC15KaceZuKcFI02").send_keys(Keys.TAB)
		time.sleep(3)
		driver.find_element(By.XPATH, "//div[@class='_1zq6UabIEJJ-z9grsiCJY7']/div[2]/textarea").send_keys(content) 
	time.sleep(5)
	driver.find_element(By.CLASS_NAME,"_18Bo5Wuo3tMV-RDB8-kh8Z").click()
		
