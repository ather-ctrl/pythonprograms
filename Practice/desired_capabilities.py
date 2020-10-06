from unittest import TestLoader, TestSuite
import HtmlTestRunner
#from Dialer_themeswitch import Dialer
#from Practice_Exercise import WhatsappAndroidTests
from ParallelTests import AndroidParallel


#example1_tests = TestLoader().loadTestsFromTestCase(Dialer)
example2_tests = TestLoader().loadTestsFromTestCase(AndroidParallel)
suite = TestSuite([example2_tests])
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False).run(suite)
