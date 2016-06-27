#!/usr/bin/python
# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import  smtplib, sys, json, urllib, urllib2


reload(sys)
sys.setdefaultencoding('utf-8')
location = "shanghai"   #位置
smtp_server = "smtp.sina.com" #smtp服务器地址
useraddr = "*******"  #发件人的邮箱地址
password = "*******"   #邮箱密码
toaddr = ["*******"]  #接收人的邮箱地址


def send_mail(to,sub,content):
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['From'] ="<"+useraddr+">"
    msg['To'] = ";".join(to)
    msg['Subject'] = sub
    try:
        server = smtplib.SMTP(smtp_server,25)
        server.login(useraddr,password)
        server.sendmail(useraddr,toaddr,msg.as_string())
        server.close()
        return True
    except Exception,e:
        print str(e)
        return False
if __name__ == '__main__':
    apikey = "77f55d3b62f0b708f79d17398904a424"
    url = 'http://apis.baidu.com/thinkpage/weather_api/suggestion?location=%s&language=zh-Hans&unit=c&start=0&days=3' %location
    req = urllib2.Request(url)
    req.add_header("apikey", apikey)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if (content):
        json_result = json.loads(content)
        list = json_result['results']
        info = list[0]['daily']
        today = info[0]
        tomorrow = info[1]
        today_date = today['date']
        tomorrow_date = tomorrow['date']
        today_text_day = today['text_day']
        tomorrow_text_day = tomorrow['text_day']
        today_text_night = today['text_night']
        tomorrow_text_night = tomorrow['text_night']
        today_high = today['high']
        tomorrow_high = tomorrow['high']
        today_low = today['low']
        tomorrow_low = tomorrow['low']

        subject = '天气预报'
        today_info = '[今天是%s,白天天气：%s,夜间天气：%s,最高气温：%s度，最低气温：%s]  ' %(today_date,today_text_day,today_text_night,today_high,today_low)
        tomorrow_info ='[明天是%s,白天天气：%s,夜间天气：%s,最高气温：%s度，最低气温：%s]  ' %(tomorrow_date,today_text_day,tomorrow_text_night,tomorrow_high,tomorrow_low)
        if send_mail(toaddr,subject,today_info) and send_mail(toaddr,subject,tomorrow_info):
            print "send msg succeed"
        else:
            print  "send msg failed"
    else:
        print "get error"



