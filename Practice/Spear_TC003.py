"""
Test case ID: 003
Test script name: Spear_TC003
Test Case Name: Login with invalid credentials, with wrong password
Test case Description: To login with invalied credential and validate.
Requirement ID: SPEAR_EVOL003
Author: Team member/Lead
Language: Python
Remarks(If any):
"""
import unittest
from appium import webdriver
import time

class Login_failed(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Samsung S9'
        desired_caps['noReset'] = 'false'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps['appPackage'] = 'com.evolgence.on'
        desired_caps['appActivity'] = 'myspear.ui.DashboardNavigationActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login_failed(self):
        time.sleep(3)
        self.driver.find_element_by_id("com.evolgence.on:id/btn_signin").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_username").send_keys("1171200001")  #Username
        self.driver.find_element_by_id("com.evolgence.on:id/edt_password").send_keys("spear@0000")  #wrong password Invalid user credentials/
        self.driver.save_screenshot('TC003_screenshot_01.png')
        self.driver.find_element_by_id("com.evolgence.on:id/btn_submit").click()
        self.driver.save_screenshot('TC003_screenshot_02.png')
        time.sleep(3)
        signin_text = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sign In']")
        login_button = self.driver.find_element_by_id("com.evolgence.on:id/btn_submit")
        self.assertTrue("Sign in page not displayed", signin_text.is_displayed())                   #pass/fail validation
        self.assertTrue("Login button not displayed", login_button.is_displayed())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_failed)
    unittest.TextTestRunner(verbosity=2).run(suite)