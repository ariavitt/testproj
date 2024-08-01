import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AviasalesCalendarTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.aviasales.ru/")

    def test_calendar_open(self):
        date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='s__hozqdl8_u1owv7f58Vov s__HLWgkBC9TdsHSs4C7GgX s__oBFQfV39usrCxG5yKxiR']"))
        )
        date_field.click()
        
        calendar = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='s__gRyRy4YyodTA5lgEQmq9 s__ZZQGOhqg9lB4emhN5Itq']"))
        )
        self.assertTrue(calendar.is_displayed(), "Календарь не отображается")

    def test_select_date(self):
        self.test_calendar_open()

        date_to_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@value,15)]"))
        )
        date_to_select.click()

        selected_date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='s__hozqdl8_u1owv7f58Vov s__HLWgkBC9TdsHSs4C7GgX s__oBFQfV39usrCxG5yKxiR']"))
        )
        self.assertIn("15", selected_date.get_attribute("value"), "Выбранная дата не отображается в поле")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
