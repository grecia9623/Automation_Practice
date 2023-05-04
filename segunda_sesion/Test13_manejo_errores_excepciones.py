import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *


class usando_unittest(unittest.TestCase):
    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    #def test_manejo_excepciones(self):
    #    driver = self.driver
    #    driver.get("http://www.google.com")
    #    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "r")))


    def test_manejo_excepciones2(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "r")))
        except TimeoutException:
            print("----- Fallo esperado!! Usando excepciones- No se encontro el elemento-----")

    # def test_buscar(self):
    #     driver = self.driver
    #     driver.get("https://www.python.org")
    #     titulo = driver.title
    #     # assert >resultado actual< in >resultado esperado<
    #     assert titulo in "Google"

    # def test_buscar2(self):
    #     driver = self.driver
    #     driver.get("https://www.python.org")
    #     titulo = driver.title
    #
    #     try:
    #         # assert >resultado actual< in >resultado esperado<
    #         assert titulo in "Google"
    #     except AssertionError:
    #         print("Error esperado --------No son titulos iguales")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

