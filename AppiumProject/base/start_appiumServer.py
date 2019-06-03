import subprocess,os
from time import ctime
from base.globalpath import appium_log_path
import psutil,time

def judgeProcess(pro_name):
    '''判断程序是否运行'''
    p = psutil.pids()
    for pid in p:
        if psutil.Process(pid).name()==pro_name:
            return True
    else:
        print("not found")
        return False

def connect_devices():
    '''连接模拟器设备'''
    # cmd = 'adb connect 127.0.0.1:62001'
    # os.popen(cmd,mode="r")
    os.system(r".\ConnectDevices.bat")

def start_MNQ(p_name):
    os.system(r".\startMNQ.bat")
    # time.sleep(10)
    if judgeProcess(p_name):
        connect_devices()
    else:
        print('devices已启动!')

def start_appium(host,port):
    '''启动appium服务'''
    bootstrap_port = str(port+1) #启动多台设备端口
    cmd = 'start /b appium -a '+ host +' -p ' + str(port)+ ' -bp '+str(bootstrap_port)  #注意前后空格
    print('%s at %s'%(cmd,ctime()))
    subprocess.call(cmd,
                     shell=True,
                     stdout=open('%s/'%appium_log_path+str(port)+'_devices.log','a'),
                     stderr=subprocess.STDOUT)

if __name__=="__main__":
    # connect_devices()
    # host = '127.0.0.1'
    # port = 4723
    # start_appium(host,port)
    # judgeProcess("Nox.exe")
    start_MNQ("Nox.exe")