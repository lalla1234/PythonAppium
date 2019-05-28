import time
from base.baseview import BaseView
from common.start_driver import StartDriver

class DriverConfig(BaseView):

    def __init__(self,driver):
        super(DriverConfig, self).__init__(driver)

    def click_operation(self):
        # 右滑
        x = int(self.drivers.get_window_size()["width"]) #x值为720，其实就是屏幕分辨率
        y = int(self.drivers.get_window_size()["height"])  #y值为1280
        s = 0
        time.sleep(2)
        while s<5:
            self.drivers.swipe(700,700,100,700,1000) #540,320,180,320  往左滑
            s+=1
        vid = self.driver.find_element_by_id("com.sxhsh:id/guide_login") #点击立即进入
        vid.click()
        time.sleep(2)
        self.drivers.save_screenshot("login.png") #截图保存到当前文件夹
        self.drivers.get_screenshot_as_file("./screenshot/login.png")

        passwd = self.drivers.find_element_by_id("com.sxhsh:id/btn_pwd_login_sms") #密码登录
        passwd.click()

        #账号输入和登录
        self.drivers.find_element_by_id("com.sxhsh:id/et_pwd_login_username").send_keys("18392031414")
        self.drivers.find_element_by_id("com.sxhsh:id/et_pwd_login_pwd").send_keys("test123456")
        self.drivers.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        self.drivers.find_element_by_id("com.sxhsh:id/iv_cell_text_with_top_icon_image").click() #class定位
        time.sleep(3)
        self.drivers.find_element_by_id("com.sxhsh:id/ll_toolbar_back_container").click() #返回
        #登录后退出
        self.drivers.find_element_by_id("com.sxhsh:id/tab5_ll").click()
        self.drivers.find_element_by_id("com.sxhsh:id/ll_setting").click() #点击设置
        self.drivers.find_element_by_xpath("//android.widget.TextView[@text='退出登录']").click() #xpath定位,android.widget.TextView
        # self.drivers.find_element_by_id("com.sxhsh:id/tab5_set_unlogin").click() #点击退出登录
        self.drivers.find_element_by_id("com.sxhsh:id/button_left").click()

        self.drivers.find_element_by_class_name("android.widget.EditText").clear() #清空输入框
        self.drivers.find_element_by_id("com.sxhsh:id/et_sms_login_username").send_keys("18392031414")
        # self.drivers.find_element_by_xpath("//android.widget.TextView[@text='发送验证码'").click()
        self.drivers.find_element_by_xpath("//*[@text='发送验证码']").click()
        # cmd = "StopAppium.bat %s"%s("http://127.0.0.1:4723/wd/hub")
        # os.popen(cmd)

if __name__=="__main__":
    strd = StartDriver()
    drivers = strd.get_driver()
    d = DriverConfig(drivers)
    result = d.click_operation()

