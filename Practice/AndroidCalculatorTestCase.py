from appium import webdriver
from threading import Thread
import time


def test(deviceName,udid, systemPorts):
    desired_caps = {}
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['systemPort'] = systemPorts
    desired_caps['deviceName'] = deviceName
    desired_caps['udid'] = udid
    desired_caps['noReset'] = 'true'
    desired_caps['appPackage'] = 'com.google.android.dialer'
    desired_caps['appActivity'] = 'com.google.android.dialer.extensions.GoogleDialtactsActivity'
    driver = webdriver.Remote('http://localhost:%s/wd/hub'%4723, desired_caps)
    driver.find_element_by_id("com.google.android.dialer:id/three_dot_menu_or_clear_icon_view").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Settings']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Display options']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.Switch[@resource-id='android:id/switch_widget']")
    driver.find_element_by_xpath("//android.widget.Switch[@text='ON']")
    driver.find_element_by_xpath("//android.widget.TextView[@text='Dark theme']").click()  # disable dark mode
    driver.quit()

class MyThread(Thread):
    def __init__(self, deviceName, udid, systemPorts):
        super(MyThread, self).__init__()
        self.deviceName = deviceName
        self.udid = udid
        self.systemPorts = systemPorts

    def run(self):
        test(self.deviceName, self.udid,self.systemPorts)

t1 = MyThread('Pixel 3a XL','8BDAX00BBD', 8201)
t2 = MyThread('Pixel 4','96141FFAZ000U9', 8202)
t1.start()
t2.start()








'''class Dialer(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['systemPort'] = '8201'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Samsung S9'
        desired_caps['Reset'] = 'true'
        desired_caps['appPackage'] = 'com.sec.android.app.popupcalculator'
        desired_caps['appActivity'] = 'com.sec.android.app.popupcalculator.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        self.driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_05").click()
        self.driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_add").click()
        self.driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_06").click()
        self.driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_equal").click()
        candy = self.driver.find_element_by_id("com.sec.android.app.popupcalculator:id/txtCalc").text
        self.assertEqual("11", candy), "Element not found"

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Dialer)
    unittest.TextTestRunner(verbosity=2).run(suite)'''