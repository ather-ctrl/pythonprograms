import unittest
from appium import webdriver
import time

class WhatsappAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Samsung S9'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        search_button = self.driver.find_element_by_xpath("//android.widget.TextView[@clickable='true']")
        search_button.click()
        time.sleep(5)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)