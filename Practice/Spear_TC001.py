"""
Test case ID: 001
Test script name: Spear_TC001
Test Case Name: Create internal ticket & delete
Test case Description: To create internal ticket and pass/fail validation
Requirement ID: EVOL_001
Author:  Team member/Lead
Language: Python
Remarks(If any):
"""
import unittest
from appium import webdriver
import time

class Login_create_delete(unittest.TestCase):
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

    def test_sp(self):
        time.sleep(3)
        self.driver.find_element_by_id("com.evolgence.on:id/btn_signin").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_username").send_keys("1171200001")  #User name
        self.driver.find_element_by_id("com.evolgence.on:id/edt_password").send_keys("spear@1234")  #Password
        self.driver.find_element_by_id("com.evolgence.on:id/btn_submit").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.evolgence.on:id/edt_company")
        self.driver.find_element_by_id("com.evolgence.on:id/edt_mobile")
        self.driver.find_element_by_id("com.evolgence.on:id/edt_email")
        self.driver.save_screenshot('TC001_screenshot_01.png')
        self.driver.find_element_by_id("com.evolgence.on:id/btn_next").click()                      #Next button
        time.sleep(6)                                                                               #loading wait time
        self.driver.find_element_by_id("com.evolgence.on:id/swipeselector_layout_swipePager")
        self.driver.find_element_by_class_name("androidx.recyclerview.widget.RecyclerView")
        self.driver.find_element_by_id("com.evolgence.on:id/navigation_apps")
        self.driver.find_element_by_xpath("//android.widget.LinearLayout//android.widget.TextView[@text='Ticketing System']").click()
        time.sleep(2)
        self.driver.save_screenshot('TC001_screenshot_02.png')
        self.driver.find_element_by_class_name("androidx.viewpager.widget.ViewPager")
        self.driver.find_element_by_id("com.evolgence.on:id/my_fab").click()
        self.driver.find_element_by_id("com.evolgence.on:id/type_me")                                 #Internal ticket
        self.driver.find_element_by_id("com.evolgence.on:id/rid1").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_category").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_search").send_keys("birth certificate")
        self.driver.find_element_by_id("com.evolgence.on:id/tv_country_name").click()
        time.sleep(2)
        self.driver.save_screenshot('TC001_screenshot_03.png')
        self.driver.find_element_by_id("com.evolgence.on:id/edt_member").click()
        self.driver.find_element_by_class_name("android.widget.TextView")
        self.driver.find_element_by_xpath("//android.widget.LinearLayout//android.widget.CheckBox[@resource-id='com.evolgence.on:id/chkbox_single']").click()
        self.driver.find_element_by_id("com.evolgence.on:id/fab_right").click()
        self.driver.find_element_by_id("com.evolgence.on:id/edt_ccmember").click()
        self.driver.find_element_by_class_name("android.widget.TextView")
        self.driver.find_element_by_xpath("//android.widget.LinearLayout//android.widget.CheckBox[@resource-id='com.evolgence.on:id/chkbox_single']").click()
        self.driver.find_element_by_id("com.evolgence.on:id/fab_right").click()
        time.sleep(2)
        self.driver.swipe(45, 1450, 45, 593)
        time.sleep(3)
        b = self.driver.find_element_by_id("com.evolgence.on:id/edt_remarks").send_keys("Query")
        self.driver.save_screenshot('TC001_screenshot_04.png')
        self.driver.find_element_by_id("com.evolgence.on:id/menu_save").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Ticketing System']")       #validating the elements/
        self.driver.find_element_by_id("com.evolgence.on:id/menu_filter")
        self.driver.find_element_by_id("com.evolgence.on:id/menu_search")
        self.driver.find_element_by_id("com.evolgence.on:id/my_fab")
        self.driver.save_screenshot('TC001_screenshot_05.png')
        self.driver.find_element_by_accessibility_id("Outbox").click()                                 #content-desc element'''
        time.sleep(1)
        self.driver.save_screenshot('TC001_screenshot_06.png')
        self.driver.find_element_by_id("com.evolgence.on:id/card_view").click()
        time.sleep(1)
        self.driver.save_screenshot('TC001_screenshot_07.png')
        self.driver.find_element_by_accessibility_id("Activity-Log")
        self.driver.find_element_by_id("com.evolgence.on:id/txt_note")
        created = self.driver.find_element_by_id("com.evolgence.on:id/txt_date")
        self.driver.find_element_by_id("com.evolgence.on:id/txt_created_by")                           #Ticket created by details validation
        self.assertTrue("Ticket Created details not displayed", created.is_displayed())                #Pass/fail verification, Ticket created validation
        self.driver.find_element_by_accessibility_id("Navigate up").click()                            #back navigation
        time.sleep(2)
        self.driver.find_element_by_id("com.evolgence.on:id/menu_option").click()                       # deleting a created ticket
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout//android.widget.TextView[@text='Delete']").click()
        time.sleep(2)
        self.driver.save_screenshot('TC001_screenshot_08.png')
        self.driver.find_element_by_id("com.evolgence.on:id/alertTitle")                                #Validating alert message and elements
        self.driver.find_element_by_id("android:id/message")
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.save_screenshot('TC001_screenshot_09.png')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login_create_delete)
    unittest.TextTestRunner(verbosity=2).run(suite)