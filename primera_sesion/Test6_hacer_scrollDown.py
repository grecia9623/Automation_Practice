import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class miclase_unittest(unittest.TestCase):

    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_hacer_scrollDown(self):
        driver = self.driver
        driver.get("https://www.oreillyauto.com")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()