import os,sys
BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)
# yaml配置文件的路径
# yamlpath = "%s\conf\driver_config.yaml"%BIR  #方式一
yamlpath = os.path.join(BIR,'conf','driver_config.yaml') #方式二
# 日志文件
log_path = BIR+"\log\log.log"
screen_path = os.path.join(BIR,'screenshots')
csvpath = os.path.join(BIR,'data','account.csv')
config_path = os.path.join(BIR,'conf','config.ini')
report_path = os.path.join(BIR,'report')
testcase_path = os.path.join(BIR,'test_case')
attach_path = os.path.join(BIR,'report') #邮件附件
appium_log_path = os.path.join(BIR,r'log\appium_log')


