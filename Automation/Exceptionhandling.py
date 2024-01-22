import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get('https://demoblaze.com')

try:
    try:
        navLogin = driver.find_element(By.ID, "login2")
        navLogin.click()
        textUsername = driver.find_element(By.ID, "loginusername")
        textUsername.send_keys("testmorning")
        textPassword = driver.find_element(By.ID, "loginpassword")
        textPassword.send_keys("test123")
        loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        loginButton.click()
    except ElementNotInteractableException as e:
        print("The try code didnot work")
        try:
            driver.implicitly_wait(10)
            textUsername = driver.find_element(By.ID, "loginuser")
            textUsername.send_keys("testmorning")
            textPassword = driver.find_element(By.ID, "loginpassword")
            textPassword.send_keys("test123")
            loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
            loginButton.click()
        except NoSuchElementException:
            print("It comes from no such element exception")
            textUsername = driver.find_element(By.ID, "loginusername")
            textUsername.send_keys("testmorning")
            textPassword = driver.find_element(By.ID, "loginpassword")
            textPassword.send_keys("test123")
            loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
            loginButton.click()

except Exception as e:
    print(e)


time.sleep(5)