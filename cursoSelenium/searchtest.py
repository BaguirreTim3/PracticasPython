from lib2to3.pgen2.driver import Driver
import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
        
     
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
        
    
    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        
     
    
    def tearDown(self):
        self.driver.quit()
        
        

if __name__ == '__main__':
    unittest.main(verbosity=2)        