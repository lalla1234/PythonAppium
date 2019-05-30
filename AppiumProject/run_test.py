import HTMLTestRunner
import unittest
from common.recordlog import logs
import time
from base.globalpath import report_path,testcase_path

if __name__=="__main__":

    load_case = unittest.defaultTestLoader.discover(testcase_path,'test_login.py') #加载用例，固定的
    # # load_case = unittest.defaultTestLoader.discover(testcase_path,'test_*.py') #模糊匹配
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_path+"\%s_%s"%(now,"testReport.html") #报告名称
    with open(report_name,'wb') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title='惠三秦UI自动化测试',description='惠三秦Android端测试用例执行结果')
        logs.info("start run test case！")
        runner.run(load_case)

