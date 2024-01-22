import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.get('https://demoblaze.com')

    def test_login(self):
        driver = self.driver
        navLogin = driver.find_element(By.ID, "login2")
        navLogin.click()
        driver.implicitly_wait(10)

        textUsername = driver.find_element(By.ID, "loginusername")
        textUsername.send_keys("testmorning")

        textPassword = driver.find_element(By.ID, "loginpassword")
        textPassword.send_keys("test123")

        loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        loginButton.click()
        time.sleep(10)
        expectedValue = "Welcome testmorning"
        actualValue = driver.find_element(By.ID, "nameofuser").text

        self.assertEqual(expectedValue, actualValue, "The user did not match")  # add assertion here

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
