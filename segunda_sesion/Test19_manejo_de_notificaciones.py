import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class miclase_unittest(unittest.TestCase):

    def setUp(self):

        s = Service("C:/chromedriver/chromedriver.exe")
        options = Options()

        # enviar argumentos(1 permitiendo la notificacion,  2 bloquean la notificacion)
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        web_driver = webdriver.Chrome(service=s, options=options)
        web_driver.maximize_window()

    def test_manejo_de_notificaciones(self):
        driver = self.driver
        driver.get("https://www.nbc.com/noticias-telemundo-en-la-noche/video/noticias-en-la-noche-07-26/9000239987")
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



