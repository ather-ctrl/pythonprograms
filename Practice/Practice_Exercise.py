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
        search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")
        search_button.click()
        name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
        name_search_box.send_keys("Shizouka")
        msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Shizouka")')
        msg.click()
        time.sleep(2)
        text_box1 = self.driver.find_element_by_id("com.whatsapp:id/entry")
        text_box1.send_keys("Searching")
        time.sleep(3)
        send_button = self.driver.find_element_by_id("com.whatsapp:id/send")
        send_button.click()
        time.sleep(8)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


#print(a)
#print("Shape: ", a.reshape(5,2))
#print("dimentions: ", a.ndim)
#print("Item size: ", a.itemsize)
#print("Data type", a.dtype)
