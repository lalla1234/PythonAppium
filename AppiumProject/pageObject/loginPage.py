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
    close_btn = (By.ID,"com.sxhsh:id/popup_advert_close_btn")
    ibtn = (By.ID,"com.sxhsh:id/tab5_ll") #我元素
    setting_btn = (By.ID,"com.sxhsh:id/ll_setting")
    logout_btn = (By.XPATH,"//android.widget.TextView[@text='退出登录']")
    button_left = (By.ID,"com.sxhsh:id/button_left") #弹框，确定
    skip_btn = (By.ID,"com.sxhsh:id/splash_tv_jump")

    def click_passwd(self):
        self.enter_butn() #点击'立即进入'
        self.driver.find_element(*self.paswd_Button).click() #点击密码登录

    # 启动app广告页
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

    # 登录页面
    def loginView(self,phone_num,password):
        self.click_passwd()
        self.skip_page()
        try:
            self.driver.find_element(*self.phonenum_element).send_keys(phone_num)
            self.driver.find_element(*self.password_element).send_keys(password)
        except NoSuchElementException:
            logs.error("No Login page element found")
            return False
        else:
            self.driver.find_element(*self.login_Button).click()
            self.getScreenshot("login")
            logs.info("login success!")
            self.logoutView()

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




if __name__=="__main__":
    driver = StartDriver().get_driver()
    login = LoginPage(driver)
    login.loginView("18392117474","test123456")