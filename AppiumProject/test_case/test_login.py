from pageObject.loginPage import LoginPage
from common.unittestFunc import UnittestFunc
from common.recordlog import logs
from common.read_csv import ReadCsvData
import unittest

class TestLogin(UnittestFunc):
    '''登录模块'''
    csv_data = ReadCsvData()

    def test_normal_case(self):
        '''正常用例'''
        logn = LoginPage(self.driver)
        data = self.csv_data.get_csv_data(1) #取配置文件中的第一行
        logn.loginView(data[0],data[1])
        self.assertTrue(logn.check_login_status())

    # @unittest.skip("skip test_phone_null")
    def test_phone_null(self):
        '''用户名为空'''
        logn = LoginPage(self.driver)
        data = self.csv_data.get_csv_data(4)
        logn.loginView(data[0], data[1])
        self.assertTrue(logn.check_login_status(),"login fail")

    # @unittest.skip("skip test_paawd_null")
    def test_paawd_null(self):
        '''密码为空'''
        logn = LoginPage(self.driver)
        data = self.csv_data.get_csv_data(4)
        logn.loginView(data[0], data[1])
        self.assertTrue(logn.check_login_status(),"login fail")

    # @unittest.skip("skip test_phone_err")
    def test_phone_err(self):
        '''用户名或密码错误'''
        logn = LoginPage(self.driver)
        data = self.csv_data.get_csv_data(7)
        logn.loginView(data[0], data[1])
        self.assertTrue(logn.check_login_status(),"login fail")

if __name__ == "__main__":
    unittest.main()