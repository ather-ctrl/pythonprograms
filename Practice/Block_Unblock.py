import unittest
from appium import webdriver
import time

class Dialer(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 3 XL'
        desired_caps['Reset'] = 'true'
        desired_caps['appPackage'] = 'com.google.android.dialer'
        desired_caps['appActivity'] = 'com.google.android.dialer.extensions.GoogleDialtactsActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):

        self.driver.find_element_by_id("com.google.android.dialer:id/three_dot_menu_or_clear_icon_view").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index='4']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.widget.TextView[@text='Blocked numbers']")
        self.driver.find_element_by_id("com.android.server.telecom:id/add_blocked").click()
        self.driver.find_element_by_id("com.android.server.telecom:id/add_blocked_number").click()
        self.driver.find_element_by_id("com.android.server.telecom:id/add_blocked_number").clear()
        time.sleep(1)
        text = '+919800000000'
        self.driver.find_element_by_id("com.android.server.telecom:id/add_blocked_number").send_keys(text)
        time.sleep(2)
        self.driver.find_element_by_id("android:id/button1").click()
        candy = self.driver.find_element_by_xpath("//android.widget.RelativeLayout//android.widget.TextView[@resource-id='com.android.server.telecom:id/blocked_number']")
        self.assertTrue(text, candy), "Element not found"
        self.driver.save_screenshot('BlockNumber.png')
        time.sleep(1)
        self.driver.find_element_by_id("com.android.server.telecom:id/delete_blocked_number").click()
        self.driver.find_element_by_id("android:id/button1").click()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Dialer)
    unittest.TextTestRunner(verbosity=2).run(suite)