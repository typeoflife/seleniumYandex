import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element_by_name("login")
        time.sleep(1)
        elem.send_keys('mylogin')
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_name('passwd')
        time.sleep(1)
        elem.send_keys('mypass')
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

if __name__ == "__main__":
    unittest.main()





