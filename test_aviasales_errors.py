import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AviasalesErrorsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.aviasales.ru/")

        openConsole = WebDriverWait(cls.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        cls.driver.execute_script("console.log('Opening console...');")
        logs = cls.driver.get_log('browser')
        errors = [entry for entry in logs if entry['level'] == 'SEVERE']
        if errors:
            print("Найдены ошибки в консоли:")
            for error in errors:
                print(error['message'])
        else:
            print("Ошибок в консоли не найдено.")


    def tearDownClass(cls):
        cls.driver.quit()