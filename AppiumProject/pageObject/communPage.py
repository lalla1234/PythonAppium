from common.common_func import CommonFunction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.recordlog import logs
from common.start_driver import StartDriver
from pageObject.loginPage import LoginPage
class CommunPage(CommonFunction):
    '''通信页面'''
    banner = (By.ID,"com.sxhsh:id/TANGRAM_VIEW_CONTAINER_ID") #通信首页banner
    flow_ball_btn = (By.ID,"com.sxhsh:id/tv_residual_flow")
    flow_btn = (By.XPATH,"//android.widget.TextView[@text='流量币']") #流量币
    exchange_btn = (By.XPATH,"//android.widget.TextView[@text='兑换']")
    exchange_flow_btn = (By.ID,"com.sxhsh:id/btn_do_exchange") #兑换流量

    # 通信首页banner广告滑动
    def sliding_banner(self):
        self.skip_page()
        try:
            banner_element = self.driver.find_element(*self.banner)
        except NoSuchElementException:
            logs.error('the banner element not found')
        else:
            banner_element.click()

    # 流量球和语音球
    def flow_ball(self):
        self.skip_page()
        try:
            self.driver.find_element(*self.flow_ball_btn).click()
            self.getScreenshot("flow")
        except NoSuchElementException:
            logs.error("the flow_ball element not found")

    # 流量币
    def flow_coin(self):
        # self.skip_page()
        try:
            self.driver.find_element(*self.flow_btn).click()
        except NoSuchElementException:
            logs.error("the flow_coin element not found")
        else:
            self.driver.find_element(*self.exchange_btn).click()
            exc_list =self.driver.find_elements(*self.exchange_flow_btn) #页面有多个相同按钮，读取列表形式在切片取值
            exc_list[1].click()
            self.getScreenshot("exchange_flow")

if __name__=="__main__":
    driver = StartDriver().get_driver()
    com = CommunPage(driver)
    com.flow_coin()