from appium import webdriver
from common.read_YamlConfig import ReadYamlConfig
from common.recordlog import logs
import os

class StartDriver(object):
    '''获取终端驱动'''
    def __init__(self):
        self.conf = ReadYamlConfig()

    def get_driver(self):
        data = self.conf.get_yamlfile()
        try:
            capabs = {}
            capabs["platformName"] = data["platformName"]
            capabs["platformVersion"] = data["platformVersion"]
            capabs["deviceName"] = data["deviceName"]
            base_dir = os.path.dirname(os.path.dirname(__file__)) #获取当前文件根目录
            app_path = os.path.join(base_dir,'app',data["appname"])
            capabs["app"] = app_path
            capabs["appPackage"] = data["appPackage"]
            capabs["appActivity"] = data["appActivity"]
            capabs["noReset"] = data["noReset"]
            capabs["automationName"] = data["automationName"] #打开这行可能会导致运行不稳定
            capabs["unicodeKeyboard"] = data["unicodeKeyboard"]
            capabs["newCommandTimeout"] = data["newCommandTimeout"]
            logs.info("start app...")
            driver = webdriver.Remote("http://%s:%s/wd/hub"%(data["ip"],data["port"]),capabs)
            # 设置隐性等待,在规定的时间内页面的所有元素都加载完了就执行下一步，否则一直等到时间截止，然后再继续下一步。
            driver.implicitly_wait(20)
            return driver
        except Exception as e:
            logs.error("Appium服务未启动或设备devices未连接!")
            driver.quit()

    def close_devices(self):
        driver = self.get_driver().close()


if __name__ =="__main__":
    dri = StartDriver()
    dri.get_driver()