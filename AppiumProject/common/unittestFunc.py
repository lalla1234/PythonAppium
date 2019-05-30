import unittest,time
from common.start_driver import StartDriver
from common.recordlog import logs

class UnittestFunc(unittest.TestCase):
    '''uinitest框架，继承TestCase'''

    def setUp(self): #每个case运行之前先运行此方法
        # logs.info("=====setUp=====")
        self.stdri = StartDriver()
        self.driver = self.stdri.get_driver()

    def tearDown(self):
        # logs.info("=====tearDown=====")
        time.sleep(5)
        self.driver.quit()

