import logging,os
from base.globalpath import log_path

def recordLogging(loggpath=None):
    '''日志模块'''
    if loggpath!=None:
        loggpath = loggpath
    loggpath = log_path
    # 实例loggers
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG) #设置日志级别
        # 日志存储在指定文件中
        fh = logging.FileHandler(loggpath,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 日志打印在屏幕
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        formt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')
        fh.setFormatter(formt)
        sh.setFormatter(formt)
        # 给logger对象添加handler
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger

logs = recordLogging()


