import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get('https://demoblaze.com')

navLogin = driver.find_element(By.ID, "login2")
navLogin.click()

textUsername = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginusername")))
textUsername.send_keys("testmorning")

textPassword = driver.find_element(By.ID, "loginpassword")
textPassword.send_keys("test123")

loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
loginButton.click()

time.sleep(5)