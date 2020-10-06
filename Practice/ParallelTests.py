caps = {}
caps['automationName'] = 'uiautomator2'
caps['platformName'] = 'Android'
caps['platformVersion'] = '10'
caps['noReset'] = 'true'
caps['appPackage'] = 'com.google.android.dialer'
caps['appActivity'] = 'com.google.android.dialer.extensions.GoogleDialtactsActivity'


import unittest
from appium import webdriver
import multiprocessing
import time


class AndroidParallel(unittest.TestCase):
    def __init__(self, method_name, deviceName, udid, systemPorts):
        super(AndroidParallel, self).__init__(method_name)
        self.deviceName = deviceName
        self.udid = udid
        self.systemPorts = systemPorts

    def setUp(self):
        desired_caps = caps.copy()
        desired_caps['systemPort'] = self.systemPorts
        desired_caps['deviceName'] = self.deviceName
        desired_caps['udid'] = self.udid
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % 4723, desired_caps)

    def tearDown(self):
        self.driver.quit()

    def themeswitch(self):
        self.driver.find_element_by_id("com.google.android.dialer:id/three_dot_menu_or_clear_icon_view").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Display options']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.Switch[@resource-id='android:id/switch_widget']")
        self.driver.find_element_by_xpath("//android.widget.Switch[@text='ON']")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click()

def tmp(suite):
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(AndroidParallel('themeswitch','Pixel 3a XL','8BDAX00BBD', 8201))

    suite2 = unittest.TestSuite()
    suite2.addTest(AndroidParallel('themeswitch','Pixel 4','96141FFAZ000U9', 8202))
    with multiprocessing.Pool(processes=2) as p:
        p.map(func=tmp,iterable=[suite1,suite2])
