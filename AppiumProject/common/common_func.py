from base.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from common.recordlog import logs
from selenium.webdriver.common.by import By # ***元素定位***
from common.start_driver import StartDriver
from base.globalpath import screen_path
import time
class CommonFunction(BaseView):
    '''公共方法，继承Baseview'''

    btn_enter = (By.ID,"com.sxhsh:id/guide_login")
    skip_btn = (By.ID, "com.sxhsh:id/splash_tv_jump")
    close_btn = (By.ID, "com.sxhsh:id/popup_advert_close_btn")
    login_key_btn = (By.ID,"com.sxhsh:id/btn_pwd_login_key")

    # 获取屏幕滑动尺寸
    def get_size(self):
        try:
            x = self.get_window_size()["width"]  # x值为720，其实就是屏幕分辨率
            y = self.get_window_size()["height"] # y值为1280,返回一个元组(720,1280)
            return x,y
        except Exception as e:
            logs.error("Failed to get screen size")

    # 检测app启动弹出广告页
    def skip_page(self):
        try:
            skip_element = self.driver.find_element(*self.skip_btn)
        except NoSuchElementException:
            pass
        else:
            self.getScreenshot("skipPage")
            skip_element.click()

    # 检查登录成功后弹框
    def check_bounced(self):
        try:
            clo_element = self.driver.find_element(*self.close_btn)
        except NoSuchElementException:
            pass
        else:
            clo_element.click()

    # 向右滑
    def swipeRight(self):
       lef = self.get_size()
       x1 = int(lef[0] * 0.9)
       y1 = int(lef[1] * 0.5)
       x2 = int(lef[0] * 0.1)
       self.get_swipe(x1,y1,x2,y1,1000)

    # 向左滑
    def swipeLeft(self):
        try:
            rig = self.get_size()
            x1 = int(rig[0] * 0.99)
            y1 = int(rig[1] * 0.99)
            x2 = int(rig[0] * 0.15)
            s = 0
            time.sleep(2)
            while s<4:
                self.get_swipe(x1,y1,x2,x1,1000)
                s+=1
        except Exception as e:
            logs.error("引导页滑动失败!")

    # 小范围滑动,获取指定区域范围
    def swipeSamll(self):
        pass

    def getTime(self):
        self.now_time = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now_time

    # 定义截图
    def getScreenshot(self,module):
        time = self.getTime()
        image_file = '%s/%s_%s.png'%(screen_path,module,time)
        logs.info("get %s screenshot"%module)
        self.driver.get_screenshot_as_file(image_file)

    def enter_butn(self): #滑动引导页，然后立即进入
        try:
            self.swipeLeft()
        except NoSuchElementException:
            # pass
            logs.error("启动失败!")
        else:
            self.find_element(*self.btn_enter).click()

    # 一键登录
    def login_key(self):
        try:
            self.find_element(*self.login_key_btn).click()
        except NoSuchElementException:
            pass

if __name__=="__main__":
    st = StartDriver()
    driver = st.get_driver()
    c = CommonFunction(driver)
    # c.swipeLeft()
    c.getScreenshot("startapp")
    c.enter_butn()