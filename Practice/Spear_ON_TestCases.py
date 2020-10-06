from unittest import TestLoader, TestSuite
import HtmlTestRunner
from Spear_TC001 import Login_create_delete
from Spear_TC002 import Login_logout
from Spear_TC003 import Login_failed

test_1 = TestLoader().loadTestsFromTestCase(Login_create_delete)  #Spear_TC001
test_2 = TestLoader().loadTestsFromTestCase(Login_logout)         #Spear_TC002
test_3 = TestLoader().loadTestsFromTestCase(Login_failed)         #Spear_TC003

suite = TestSuite([test_1, test_2, test_3])
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False).run(suite)
