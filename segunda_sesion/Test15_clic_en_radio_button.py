import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver= webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_clic_en_radio_button(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        try:
            #radio_btn= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")))
            radio_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/div[3]/label[2]/span")))
            radio_btn.click()
        finally:
            print("-----El elemento no se encontro-----")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
