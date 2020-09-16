from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys

#secrets

username = "Your email"
password = "Your password"

#browser configurations
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
driver.maximize_window()

#Login Proceeds
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div[2]/form/div[1]/input'))).send_keys(username)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div[2]/form/div[2]/input'))).send_keys(password)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/main/div[2]/form/div[3]/button"))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[8]/aside/div/header"))).click()

#my network tab
driver.get('https://www.linkedin.com/mynetwork/')
time.sleep(5)

#scroll to 1/8-350 to make that element clickable
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/8-350);")
driver.find_element_by_xpath("/html/body/div[8]/div[5]/div/div/div/div/div/div/ul/li[2]/div/button").click()
time.sleep(3)

#popup menu
popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

#scroll to load HTML elements
stat = 100
for i in range(100):
	driver.execute_script(f"arguments[0].scrollTo(0,{str(stat)})",popup)
	time.sleep(0.25)
	stat += 100

#obtained list
lists = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul')
time.sleep(4)


#Started connecting!!
for start,people in enumerate(lists.find_elements_by_tag_name('li')[0:],start=1):
	people.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/li[{start}]/div/section/div[2]/footer').click()
	time.sleep(1)# 1 connections per second