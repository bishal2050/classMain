
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get('https://demoblaze.com')