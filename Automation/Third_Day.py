import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Alerts.html')

simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simple_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button1.click()
time.sleep(5)
alt = driver.switch_to.alert
alt.accept()
time.sleep(5)

confirm_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confirm_nav.click()
button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button2.click()
time.sleep(5)
alt.dismiss()
time.sleep(5)

prompt_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
prompt_nav.click()
button3 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button3.click()
time.sleep(5)
alt.send_keys("class 930 am")
alt.accept()
time.sleep(5)