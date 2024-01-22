import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from page.LoginPage import login

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("C:\\Selenium\\chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.get('https://demoblaze.com')

    def test_login(self):
        lp = login(self.driver)
        lp.userLogin("testmorning", "test123")
        time.sleep(10)
        expectedValue = "Welcome testmorning"
        actualValue = self.driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expectedValue, actualValue, "The user did not match")

    def tearDown(self) -> None:
        self.driver.quit()





if __name__ == '__main__':
    unittest.main()
