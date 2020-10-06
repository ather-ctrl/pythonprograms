import unittest
from selenium import webdriver
import pytest

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")
        inst.driver.title()

    @pytest.mark.run(order=1)
    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Selenium Webdriver interview questions")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("r")
        self.assertTrue(11, len(lists))

    @pytest.mark.run(order=2)
    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertTrue(11, len(list_new))

    @pytest.mark.run(order=3)
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()