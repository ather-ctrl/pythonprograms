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
        self.driver.find_element_by_id("com.google.android.dialer:id/three_dot_menu_or_clear_icon_view").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Display options']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.Switch[@resource-id='android:id/switch_widget']")
        candy = self.driver.find_element_by_xpath("//android.widget.Switch[@text='ON']")
        self.assertTrue('ON', candy), "Element not found"
        self.driver.save_screenshot('sana.png')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click() #disable dark mode

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Dialer)
    unittest.TextTestRunner(verbosity=2).run(suite)