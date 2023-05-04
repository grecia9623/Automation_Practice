import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_manejo_de_cookies(self):
        driver = self.driver
        driver.get("https://www.nbc.com/noticias-telemundo-en-la-noche/video/noticias-en-la-noche-07-26/9000239987")

        mis_cookies=driver.get_cookies()
        print("estas son mis cookies viejo!!! ")
        for cookie in mis_cookies:
            print(cookie)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
