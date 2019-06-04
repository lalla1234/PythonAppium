import subprocess,os
from time import ctime
from base.globalpath import appium_log_path
import psutil,time


def judgeProcess(pro_name):
    '''查看程序是否运行'''
    p = psutil.pids()
    for pid in p:
        if psutil.Process(pid).name()==pro_name:
            return True
    else:
        print("not found")
        return False

def connect_devices():
    '''连接设备devices'''
    # cmd = 'adb connect 127.0.0.1:62001'
    # os.popen(cmd,mode="r")
    os.system(r".\ConnectDevices.bat")

def start_MNQ(p_name):
    os.system(r".\startMNQ.bat")
    # time.sleep(10)
    if judgeProcess(p_name):
        connect_devices()
    else:
        print('devices??????!')

def kill_AppiumS(port):
    '''查看进程ID'''
    try:
        process = os.popen("netstat -aon |findstr %s"%port).read()
        pid = process.split()[4]
        print("%s端口的进程ID为: \033[31;1m%s\033[0m"%(port,pid))
    except Exception as e:
        print("not found port")

def stop_process(pro_id):
    '''停止进程'''
    try:
        os.system("taskkill -f -pid %s" %pro_id) #显示乱码，可在setting->editor->File Encodings->设置global_encoding设置GBK
    except Exception:
        print("not found process")


def kill_AppiumS(port):
    '''查看appium进程ID'''
    try:
        process = os.popen("netstat -aon |findstr %s"%port).read()
        pid = process.split()[4]
        print("%s端口的进程ID为: \033[31;1m%s\033[0m"%(port,pid))
    except Exception as e:
        print("not found port")

def start_appium(host,port):
    '''启动appium服务'''
    bootstrap_port = str(port+1) #启动多个端口
    cmd = 'start /b appium -a '+ host +' -p ' + str(port)+ ' bootstrap-port '+str(bootstrap_port)  #注意前后空格
    print('%s at %s'%(cmd,ctime()))
    p = subprocess.Popen(cmd,
                     shell=True,
                     stdout=open('%s/'%appium_log_path+str(port)+'_devices.log','a',),
                     stderr=subprocess.STDOUT)
    p.wait()


if __name__=="__main__":
    connect_devices()
    # start_MNQ("Nox.exe")
    # host = '127.0.0.1'
    # port = 4723
    # start_appium(host,port)
    # judgeProcess("Nox.exe")
    # kill_AppiumS(4723)
    # stop_process(8444)

