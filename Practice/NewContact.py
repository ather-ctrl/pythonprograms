import unittest
from appium import webdriver
import time

class Dialer(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 4'
        desired_caps['Reset'] = 'true'
        desired_caps['appPackage'] = 'com.google.android.dialer'
        desired_caps['appActivity'] = 'com.google.android.dialer.extensions.GoogleDialtactsActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        self.driver.find_element_by_id("com.google.android.dialer:id/contacts_tab").click()
        self.driver.find_element_by_id("com.google.android.dialer:id/contact_name").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='First name']").send_keys("Test")
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Last name']").send_keys("Contact")
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Phone']").send_keys("+123456890")
        self.driver.find_element_by_id("com.google.android.contacts:id/menu_save").click()
        self.driver.save_screenshot('NewContact.png')
        candy = self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.widget.TextView[@text='Test Contact']")
        #wafer = self.driver.find_element_by_xpath("//android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.google.android.contacts:id/header']")
        self.assertTrue('Test Contact', candy), "Element not found"
        #self.assertEqual('com.google.android.contacts:id/header', wafer), "Element not found"
        self.driver.find_element_by_accessibility_id("More options").click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout//android.widget.TextView[@resource-id='com.google.android.contacts:id/title']").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.save_screenshot('DeleteContact.png')
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Dialer)
    unittest.TextTestRunner(verbosity=2).run(suite)