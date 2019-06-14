from common.recordlog import logs
from selenium.webdriver.support.ui import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions as EC

class BaseView(object):

    def __init__(self,driver):
        self.driver = driver

    # 查找元素
    def find_element(self,*loc):
        # try:
        #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))  # 显示等待
        #     return self.driver.find_element(*loc)
        # except Exception as e:
        #     logs.error('页面未找到%s元素'%loc)
        return self.driver.find_element(*loc)

    # 获取content-desc元素
    def find_element_by_accessibility_id(self,loc):
        return self.driver.find_element_by_accessibility_id(loc)

    # 查找元素列表
    def find_elements(self,*loc):
        # try:
        #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))  # 显示等待
        #     return self.driver.find_elements(*loc)
        # except Exception as e:
        #     logs.error('页面未找到%s元素'%loc)
        return self.driver.find_elements(*loc)

    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动屏幕
    def get_swipe(self,start_x, start_y, end_x, end_y, duration=None): #对原生方法二次封装，duration持续的时间
        return self.driver.swipe(start_x, start_y, end_x, end_y,duration)

    # H5页面元素
    def get_H5element(self,cont):
        # H5上下文
        contexts = self.driver.contexts
        print("contexts：",contexts)
        # 切换进webview视图
        if cont in contexts:
            self.driver.switch_to.context(cont)
            return True
        else:
            print("没有找到对应webview!")
            return False

    # 切换到默认的context
    def switch_to_default(self):
       return self.driver.switch_to.context("NATIVE_APP")




