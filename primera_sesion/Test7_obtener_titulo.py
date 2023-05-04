import unittest #Paquete con muchas funciones
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#
class miclase_unittest(unittest.TestCase): #Pasarle las funciones de unittest

    #Si pertenece a una clase estan relacionadas
    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_obtener_titulo(self):
        driver = self.driver
        driver.get("https://www.oreillyauto.com")
        titulo = driver.title
        print("El titulo de la pagina es: " + titulo)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()