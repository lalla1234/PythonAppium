import subprocess
from time import ctime
from base.globalpath import appium_log_path

def start_appium(host,port):
    '''启动appium服务'''
    ports = str(port+1) #启动多台设备端口
    cmd = 'start /b appium -a '+ host +' -p ' + str(port)+ ' -bp '+str(ports)  #注意前后空格
    print('%s at %s'%(cmd,ctime()))
    subprocess.Popen(cmd,
                     shell=True,
                     stdout=open('%s/'%appium_log_path+str(port)+'_devices.log','a'),
                     stderr=subprocess.STDOUT)


if __name__=="__main__":
    host = '127.0.0.1'
    port = 4723
    start_appium(host,port)