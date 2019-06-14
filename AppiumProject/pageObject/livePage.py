from common.common_func import CommonFunction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.recordlog import logs
from common.start_driver import StartDriver
from time import sleep
import pytesser3
from PIL import Image,ImageEnhance

class LivePage(CommonFunction):
    '''生活模块页面操作封装'''
    live_btn = (By.ID,"com.sxhsh:id/tab2_ll")
    ill_btn = (By.CLASS_NAME,"android.widget.ImageView")
    car_btn = ("机动车违法查询") #通过content-desc定位
    car_title = (By.ID,"com.sxhsh:id/tv_toolbar_title")

    # 机动车违法查询
    def illegal_query(self):
        self.check_bounced()
        self.driver.find_element(*self.live_btn).click()
        try:
            query = self.find_elements(*self.ill_btn)
        except NoSuchElementException:
            print("not found ill_btn element")
        else:
            query[9].click()
            self.find_element_by_accessibility_id(self.car_btn).click()
            try:
                self.find_element(*self.car_title)
            except NoSuchElementException:
                pass
            else:
                sleep(1)
                self.driver.get_screenshot_as_file("..\screenshots\car_page.png")

    # 识别图片验证码
    def get_Verification_code(self):
        self.illegal_query()
        # 裁剪页面上的验证码图片
        imgScreen = Image.open("..\screenshots\car_page.png")
        box = (726,678,960,774)   #设置要裁剪的区域，可在UI Automator元素列表bounds中查看
        img = imgScreen.crop(box)  # 裁剪得到一个新的图片
        img.save('..\screenshots\indent.png')  #保存新的图像
        #------------识别新图像上的验证码---------------------------
        im = Image.open('..\screenshots\indent.png')
        imgry = im.convert('L')  # 把彩色图像转化为灰度图像。RBG转化到HSI彩色空间
        # imgry.load()
        trshold = 170 #灰度阈值设置170，低于这个值的点全部填白色，这个值是关键
        table = []
        for j in range(256):
            if j<trshold:
                table.append(0)
            else:
                table.append(1)
        bim = imgry.point(table,'1')
        bim.save('..\screenshots\indent.png') #二值化处理后重新保存
        # 使用ImageEnhance可以增强图片的识别率,对比度增强
        sharpness = ImageEnhance.Contrast(imgry)
        sharpness.enhance(1.0)
        # 锐度增强
        imgen = ImageEnhance.Sharpness(imgry)
        imgen.enhance(4.0)
        sleep(2)
        # code = pytesseract.image_to_string(shar_img)
        code = pytesser3.image_file_to_string('..\screenshots\indent.png').strip()
        print(code)



if __name__ == '__main__':
    driver = StartDriver().get_driver()
    live = LivePage(driver)
    print(live.get_Verification_code())