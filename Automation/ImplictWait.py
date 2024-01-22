import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get('https://demoblaze.com')

navLogin = driver.find_element(By.ID, "login2")
navLogin.click()
driver.implicitly_wait(10)

textUsername = driver.find_element(By.ID, "loginusername")
textUsername.send_keys("testmorning")

textPassword = driver.find_element(By.ID, "loginpassword")
textPassword.send_keys("test123")

loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
loginButton.click()

time.sleep(5)