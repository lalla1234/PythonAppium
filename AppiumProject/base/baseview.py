from common.recordlog import logs
class BaseView(object):

    def __init__(self,driver):
        self.driver = driver

    # 查找元素
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    # 查找元素列表
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动屏幕
    def get_swipe(self,start_x, start_y, end_x, end_y, duration=None): #对原生方法二次封装，duration持续的时间
        return self.driver.swipe(start_x, start_y, end_x, end_y,duration)
