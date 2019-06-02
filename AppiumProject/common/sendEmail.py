from common.getConfig import ConfigData
from common.recordlog import logs
import smtplib
from email.mime.text import MIMEText #构建邮件格式
from email.mime.multipart import MIMEMultipart  #带附件
from base.globalpath import attach_path

class SendEmail(object):

    conf = ConfigData()

    def __init__(self):
        self.host = self.conf.get_email("host")
        self.sender_eml = self.conf.get_email("sender_email")
        self.passwd = self.conf.get_email("password")
        self.recipient_list = self.conf.get_recipients("recipients")
        self.subject = self.conf.get_email('subject')
        self.content = self.conf.get_email('emicontent')

    def send_email(self,reports):
        sender = "yzm<%s>"%(self.sender_eml)
        mtp = MIMEMultipart() #带附件实例
        mtp['Subject'] = self.subject
        mtp['From'] = sender
        mtp['To'] = ';'.join(self.recipient_list) #收件人
        # 构造文字内容邮件
        mtp.attach(MIMEText(self.content,_subtype='plain',_charset='utf-8'))
        # 构造附件
        attach_file = reports #报告文件
        mit = MIMEText(open(attach_file,'rb').read(),'base64','utf-8')
        mit['Content-Type'] = 'application/octet-stream'
        mit['Content-Disposition'] = 'attachment; filename="hsq_UIAutoTestReport.html"'  #附件重命名
        mtp.attach(mit)
        # 发送邮件
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(self.sender_eml,self.passwd)
            server.sendmail(sender,self.recipient_list,mtp.as_string())
        except Exception as e:
            logs.error(e)
        else:
            server.quit()

if __name__=="__main__":
    s = SendEmail()
    s.send_email('2019-05-31 10_23_00_testReport')

