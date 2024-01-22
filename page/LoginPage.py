import time

from locator.Locator import locate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login:
    def __init__(self, driver):
        self.brower = driver
        self.lc = locate()


    def userLogin(self,username,password):
        driver = self.brower
        lc = self.lc
        navLogin = driver.find_element(By.ID, lc.login_nav_bar_id)
        navLogin.click()
        driver.implicitly_wait(10)
        textUsername = driver.find_element(By.ID, lc.login_username_id)
        textUsername.send_keys(username)
        textPassword = driver.find_element(By.ID, lc.login_password_id)
        textPassword.send_keys(password)
        loginButton = driver.find_element(By.XPATH, lc.login_button_xpath)
        loginButton.click()

