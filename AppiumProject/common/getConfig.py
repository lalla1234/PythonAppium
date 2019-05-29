import configparser
from common.recordlog import logs
from base.globalpath import config_path

class ConfigData(object):

    def __init__(self):
        self.conf = self.get_config_obj()

    def get_config_obj(self):
        conf_obj = configparser.ConfigParser()
        conf_obj.read(config_path,encoding='utf-8')
        return conf_obj

    def get_values(self,sec_name,opt_name):
        try:
            return self.conf.get(sec_name,opt_name)
        except Exception as e:
            logs.error(e)

if __name__=="__main__":
    c = ConfigData()
    result = c.get_values("email","host")
    print(result)