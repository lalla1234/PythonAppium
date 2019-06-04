from common.recordlog import logs
from common.start_driver import StartDriver
from selenium.webdriver.common.by import By
from common.common_func import CommonFunction
from selenium.common.exceptions import NoSuchElementException

class LoginPage(CommonFunction):

    paswd_Button = (By.ID,"com.sxhsh:id/btn_pwd_login_sms")
    phonenum_element = (By.ID,"com.sxhsh:id/et_pwd_login_username")
    password_element = (By.ID,"com.sxhsh:id/et_pwd_login_pwd")
    login_Button = (By.CLASS_NAME,"android.widget.Button")
    ibtn = (By.ID,"com.sxhsh:id/tab5_ll") #我元素
    setting_btn = (By.ID,"com.sxhsh:id/ll_setting")
    logout_btn = (By.XPATH,"//android.widget.TextView[@text='退出登录']")
    button_left = (By.ID,"com.sxhsh:id/button_left") #弹框，确定

    phone_tv = (By.ID,"com.sxhsh:id/tab5_phone_tv")#登录成功后检测手机号

    def click_passwd(self):
        self.enter_butn() #点击'立即进入'
        self.driver.find_element(*self.paswd_Button).click() #点击密码登录

    # 登录页面
    def loginView(self,phone_num,password):
        self.click_passwd()
        self.skip_page()
        try:
            self.driver.find_element(*self.phonenum_element).send_keys(phone_num)
            self.driver.find_element(*self.password_element).send_keys(password)
        except NoSuchElementException:
            logs.error("No Login page element found")
        else:
            self.driver.find_element(*self.login_Button).click()
            self.getScreenshot("login")
            # logs.info("login success!")
            # self.logoutView()

    # 退出登录
    def logoutView(self):
        try:
            self.check_bounced()
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.ibtn).click()
            self.driver.find_element(*self.setting_btn).click()
            self.driver.find_element(*self.logout_btn).click()
            self.driver.find_element(*self.button_left).click()
            logs.info("logout success!")
            self.getScreenshot("logout")

    # 检查登录状态
    def check_login_status(self):
        try:
            self.driver.find_element(*self.ibtn).click()
            self.find_element(*self.phone_tv)
        except NoSuchElementException:
            logs.info("login fail!")
            self.getScreenshot('login fail') #失败截图
            return False
        else:
            logs.info("login success!")
            return True


if __name__=="__main__":
    driver = StartDriver().get_driver()
    login = LoginPage(driver)
    login.loginView("18392117474","test123456")