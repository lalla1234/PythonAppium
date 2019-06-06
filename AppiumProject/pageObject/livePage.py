from common.common_func import CommonFunction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.recordlog import logs
from common.start_driver import StartDriver

class LivePage(CommonFunction):
    '''生活模块页面操作封装'''
    pass










if __name__ == '__main__':
    driver = StartDriver().get_driver()