import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver= webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_usando_css_selector(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/default.asp")
        time.sleep(5)
        content = driver.find_element(By.CSS_SELECTOR, 'a.w3-blue') #HTML Quiz Test
        print(content.text)
        content.click()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()









