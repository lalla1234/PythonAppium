from common.recordlog import logs
from common.start_driver import StartDriver
from selenium.webdriver.common.by import By
from common.common_func import CommonFunction

class LoginPage(CommonFunction):

    paswd_Button = (By.ID,"com.sxhsh:id/btn_pwd_login_sms")
    username_element = (By.ID,"com.sxhsh:id/et_pwd_login_username")
    password_element = (By.ID,"com.sxhsh:id/et_pwd_login_pwd")
    login_Button = (By.CLASS_NAME,"android.widget.Button")

    def click_passwd(self):
        self.enter_butn() #点击'立即进入'
        self.find_element(*self.paswd_Button).click()

    def loginView(self,username,password):
        self.click_passwd()
        self.find_element(*self.username_element).send_keys(username)
        self.find_element(*self.password_element).send_keys(password)
        self.find_element(*self.login_Button).click()

if __name__=="__main__":
    driver = StartDriver().get_driver()
    login = LoginPage(driver)
    login.loginView("18392117474","test123456")