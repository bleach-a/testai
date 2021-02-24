import time
from email.mime.multipart import MIMEMultipart

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib import request
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
import os
import threading
# 打开Chrome浏览器

option = ChromeOptions()     #实例化一个ChromeOptions对象
option.add_experimental_option('excludeSwitches', ['enable-automation'])  #以键值对的形式加入参数
browser = webdriver.Chrome(options=option)
browser.get("http://www.778faka.com/links/0977D47E")
browser.maximize_window()



def fun_timer():
    # global timer

    # 下拉菜单的选择
    browser.refresh()
    browser.implicitly_wait(30)
    browser.find_element_by_link_text("关闭").click()
    s1 = Select(browser.find_element_by_id('cateid'))
    # s1.select_by_value("1301")
    s1.select_by_value("1416")

    browser.implicitly_wait(30)
    s2 = Select(browser.find_element_by_id('goodid'))
    # s2.select_by_value("3214")
    s2.select_by_value("3582")

    # browser.implicitly_wait(30)
    # key = browser.find_element_by_class_name("spsm span span").text[2]

    #有货时候触发
    browser.find_element_by_class_name("phone_num").send_keys(13260219052)
    #点击确认支付，并付款截图
    browser.implicitly_wait(30)
    browser.find_element_by_id("check_pay").click()

    time.sleep(3)
    # browser.switch_to.window(browser.window_handles[0])
    browser.switch_to.frame("nyroModalIframe")
    # browser.find_element_by_id("pay_btn").click()
    # browser.find_element_by_link_text("确认付款").click()
    browser.find_element_by_xpath("// *[ @ id = 'pay_btn']")
    browser.implicitly_wait(30)
    browser.get_screenshot_as_file(r"screenPicture1.png")


    #将图片发送到邮件

    def sendMail():
        my_sender = '984940461@qq.com'  # 发件人邮箱账号
        my_pass = 'zjjcnximtttmbfaf'  # 发件人邮箱密码amazetbeobezbgah qbzjfseinsyrbchc
        my_user = '864874853@qq.com'  # 收件人邮箱账号，我这边发送给自己
        url = str(request.urlopen(r'http://txt.go.sohu.com/ip/soip').read())
        ip = re.findall(r'\d+.\d+.\d+.\d+', url)
        print(ip[0])

        def mail(ip):
            ret = True
            try:
                # msg = MIMEMultipart()
                # content = MIMEText(ip[0], 'plain', 'utf-8')  # 正文
                # msg.attach(content)
                img_file = open("screenPicture1.png", "rb")
                sendimagefile = img_file.read()
                msg = MIMEImage(sendimagefile)
                msg.add_header('Content-ID', '<image1>')
                msg.add_header('Content-Disposition', 'attachment', filename='二维码.png')
                msg['From'] = formataddr(["堕落天使", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['To'] = formataddr(["邪神·洛基", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['IP'] = "一居室"  # 邮件的主题，也可以说是标题

                # 账户密码
                server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
                server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

                server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()  # 关闭连接
            except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                ret = False
            return ret

        ret = mail(ip)
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
    if int(key) != 0:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print(key)
        browser.implicitly_wait(30)
        # browser.find_element_by_class_name(".phone_num")

        sendMail(picture)
        # timer.cancel()
        # browser.quit()
        # os.system("shutdown -s -t 600")


    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print("库存为0")

#     timer = threading.Timer(300, fun_timer)
#     timer.start()
#
#
# timer = threading.Timer(300, fun_timer)
# timer.start()


fun_timer()
