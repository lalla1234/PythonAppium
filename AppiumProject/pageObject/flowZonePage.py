from common.common_func import CommonFunction
from common.recordlog import logs
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.start_driver import StartDriver

class FlowZone(CommonFunction):
    '''通信首页-流量专区页面'''
    btn = (By.XPATH,"//android.widget.TextView[@text='流量专区']")
    image_btn = (By.ID,"com.sxhsh:id/image")
    imageView = (By.ID,"com.sxhsh:id/imageView")
    handle_btn = (By.ID,"com.sxhsh:id/tv_toHandle")
    comfirm_btn = (By.XPATH,"//*[text='确认办理']")

    def flow_zone_btn(self):
        # self.skip_page()
        self.check_bounced()
        try:
            btns = self.driver.find_element(*self.btn)
        except NoSuchElementException:
            logs.error("the btns element not found")
        else:
            btns.click()

    def flow_handle(self):
        self.login_key()
        self.flow_zone_btn()
        try:
           imags = self.driver.find_elements(*self.image_btn)
        except NoSuchElementException:
            logs.error("not found image_btn")
        else:
            for item in imags:
                sleep(0.5)
                item.click()
            imags[1].click()
            self.driver.find_elements(*self.imageView)[0].click()
            try:
                self.find_element(*self.handle_btn).click()
            except NoSuchElementException:
                logs.error("not found handle_btn element")
            self.get_H5element()
            # self.find_element(*self.comfirm_btn).click()

if __name__ == '__main__':
    driver = StartDriver().get_driver()
    flow = FlowZone(driver)
    flow.flow_handle()