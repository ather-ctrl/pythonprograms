"""
Test case ID: 002
Test script name: Spear_TC002
Test Case Name: Login & logout
Test case Description: To varify login & logout
Requirement ID: SPEAR_EVOL002
Author: Team member/Lead
Language: Python
Remarks(If any):
"""
import unittest
from appium import webdriver
import time

class Login_logout(unittest.TestCase):
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

    def test_login_logout(self):
        time.sleep(3)
        self.driver.find_element_by_id("com.evolgence.on:id/btn_signin").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_username").send_keys("1171200001")  #User name
        self.driver.find_element_by_id("com.evolgence.on:id/edt_password").send_keys("spear@1234")  #Password
        self.driver.find_element_by_id("com.evolgence.on:id/btn_submit").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.evolgence.on:id/edt_company")
        self.driver.find_element_by_id("com.evolgence.on:id/edt_mobile")
        self.driver.find_element_by_id("com.evolgence.on:id/edt_email")
        self.driver.save_screenshot('TC002_screenshot_01.png')
        self.driver.find_element_by_id("com.evolgence.on:id/btn_next").click()                       #Next button
        time.sleep(8)                                                                                #loading time
        self.driver.find_element_by_id("com.evolgence.on:id/swipeselector_layout_swipePager")
        self.driver.find_element_by_class_name("androidx.recyclerview.widget.RecyclerView")
        self.driver.find_element_by_id("com.evolgence.on:id/navigation_apps")
        time.sleep(2)
        self.driver.save_screenshot('TC002_screenshot_02.png')
        self.driver.find_element_by_accessibility_id("Profile").click()
        self.driver.find_element_by_id("com.evolgence.on:id/txtSubTitle")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='About']")
        self.driver.save_screenshot('TC002_screenshot_03.png')
        self.driver.find_element_by_id("com.evolgence.on:id/txtSubTitle")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Logout']").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.evolgence.on:id/alertTitle")
        self.driver.find_element_by_id("android:id/message")
        self.driver.find_element_by_id("android:id/button2")
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.save_screenshot('TC002_screenshot_04.png')
        time.sleep(4)
        otp_button = self.driver.find_element_by_id("com.evolgence.on:id/btn_otp")
        signin_button = self.driver.find_element_by_id("com.evolgence.on:id/btn_signin")
        self.assertTrue("Signin button not displayed", signin_button.is_displayed())                     #pass/fail validation/verification
        self.assertTrue("OTP button not displayed", otp_button.is_displayed())
        self.driver.save_screenshot('TC002_screenshot_05.png')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_logout)
    unittest.TextTestRunner(verbosity=2).run(suite)