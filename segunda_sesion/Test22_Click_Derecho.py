import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_click_derecho(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Harry_Potter")

        clickDerecho = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/p[1]/i/b")
        actions = ActionChains(self.driver)
        actions.context_click(clickDerecho).perform()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
