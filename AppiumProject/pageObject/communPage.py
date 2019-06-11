from common.common_func import CommonFunction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.recordlog import logs
from common.start_driver import StartDriver
from selenium.webdriver.support.ui import WebDriverWait

class CommunPage(CommonFunction):
    '''通信页面'''
    banner = (By.ID,"com.sxhsh:id/TANGRAM_VIEW_CONTAINER_ID") #通信首页banner
    flow_ball_btn = (By.ID,"com.sxhsh:id/tv_residual_flow")
    flow_btn = (By.ID,"com.sxhsh:id/iv_cell_text_with_top_text_corner") #流量币
    exchange_btn = (By.XPATH,"//android.widget.TextView[@text='兑换']")
    exchange_flow_btn = (By.ID,"com.sxhsh:id/btn_do_exchange") #兑换流量
    button_left = (By.ID,"com.sxhsh:id/button_left") #弹框点击确认
    back_btn = (By.ID,"com.sxhsh:id/iv_toolbar_back_icon")
    flow_total_ele = (By.XPATH,"//android.widget.TextView[@resource-id='com.sxhsh:id/tv_user_total_coin']") #流量币总数
    phone_pay_ele = (By.CLASS_NAME,"android.webkit.WebView")
    phone_pay_btn = (By.XPATH, "//android.widget.TextView[@text='缴话费']")
    input_phone = (By.ID,"serialNumber")

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

    # 流量币总数
    # def flow_total(self):
    #     try:
    #         flows = self.driver.find_elements(*self.flow_btn)
    #         flows[2].click()
    #         ele = self.driver.find_element(*self.flow_total_ele)
    #         total = int(ele.get_attribute("text"))
    #     except NoSuchElementException:
    #         logs.error("not found flow_total_element")
    #     else:
    #         return total

    # 流量币
    def flow_coin(self):
        # self.login_key()
        # self.skip_page()
        # self.check_bounced()
        try:
            flows = self.driver.find_elements(*self.flow_btn)
        except NoSuchElementException:
            logs.error("the flow_btn element not found")
        else:
            flows[2].click()
            self.driver.find_element(*self.exchange_btn).click()
            exc_list =self.driver.find_elements(*self.exchange_flow_btn) #页面有多个相同按钮，读取列表形式在切片取值
            try:
                exc_list[1].click()
                btn_left =self.driver.find_element(*self.button_left) #确认兑换提示框
            except NoSuchElementException:
                logs.info("流量币不足或已抢光!")
                self.getScreenshot("flowNotEnough")
            else:
                btn_left.click()
                total = self.driver.find_element(*self.flow_total_ele).get_attribute("text")
                self.getScreenshot("exchange_flow")
                return int(total)

    # 验证流量币是否兑换成功
    def check_flow_exchange_successful(self):
        try:
            self.driver.find_elements(*self.flow_btn)[2].click()
            ele = self.driver.find_element(*self.flow_total_ele)
            flow_coin_total = int(ele.get_attribute("text"))
        except NoSuchElementException:
            logs.error("the flow_btn element not found")
            return None
        else:
            self.find_element(*self.back_btn).click()
            return flow_coin_total

    # 话费支付
    def phone_pay(self):
        try:
            self.driver.find_element(*self.phone_pay_btn).click()
            # self.driver.find_element(*self.phone_pay_ele)
            # 显示等待
            WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.sxhsh:id/webview'))
        except NoSuchElementException:
            logs.error("not found phone_pay_ele element")
        else:
            self.get_H5element("WEBVIEW_com.android.browser")
            self.driver.find_element(*self.input_phone).send_keys('18293117474')
            # self.switch_to_default()


if __name__=="__main__":
    driver = StartDriver().get_driver()
    com = CommunPage(driver)
    print(com.phone_pay())
    # print(com.check_flow_exchange_successful())