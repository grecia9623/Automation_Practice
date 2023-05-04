import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class miclase_unittest(unittest.TestCase):
	def setUp(self):
		s = Service("C:/chromedriver/chromedriver.exe")
		self.driver = webdriver.Chrome(service=s)
		self.driver.maximize_window()

	def test_buscar(self):
		driver= self.driver
		driver.get("https://www.python.org")
		assert "Welcome to Python.org" == driver.title, "Error en el titulo"

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

