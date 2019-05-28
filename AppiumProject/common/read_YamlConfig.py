import yaml
from base.globalpath import yamlpath
from common.recordlog import logs

class ReadYamlConfig(object):
    '''读取Yaml格式文件'''
    def __init__(self,yaml_file=None):
        if yaml_file!=None:
            self.yaml_file = yaml_file
        else:
            self.yaml_file = yamlpath

    def get_yamlfile(self):
        with open(self.yaml_file,'r',encoding='utf-8') as yf:
            data = yaml.load(yf,Loader=yaml.FullLoader)
        return data


    # def get_for_deriver_data(self,drivername):
    #     driverdata = self.global_data[drivername]
    #     return driverdata


if __name__ =="__main__":
    r = ReadYamlConfig()
    result = r.get_yamlfile()
    print(result["deviceName"])