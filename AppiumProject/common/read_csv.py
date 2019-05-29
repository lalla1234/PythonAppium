import csv
from common.recordlog import logs
from base.globalpath import csvpath

class ReadCsvData(object):

    def __init__(self,csvfile=None):
        if csvfile!=None:
            self.csvfile = csvfile
        self.csvfile = csvpath

    def get_csv_data(self,line):
        try:
            with open(self.csvfile,'r',encoding='utf-8-sig') as cf:
                data = csv.reader(cf)
                for index,items in enumerate(data,1): #从索引1开始
                    if index == line:
                        return items
        except Exception as e:
            logs.error(e)

if __name__=="__main__":
    r = ReadCsvData()
    print(r.get_csv_data(1))