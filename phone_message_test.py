# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 11:25
# @Author  : collen
import requests, sys
host = 'https://api.ums86.com:9600/sms/Api/Send.do'
SpCode = '220741'
LoginName = 'wly-jfjk'
Password = 'wly_88888'
MessageContent = ''
UserNumber = '18328381861|18224460144'
SerialNumber = '1'


def send_message(user_phone, contents):
    """发送短信"""
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    data = {'SpCode': SpCode, 'LoginName': LoginName, 'Password': Password, 'MessageContent': contents, 'UserNumber': user_phone, 'SerialNumber': SerialNumber}
    return requests.post(host, data=data, headers=headers)


def get_problem_message():
    """得到告警信息"""
    user_phone = UserNumber.replace("|", ",")
    ip = sys.argv[1]
    msg = sys.argv[2]
    dot = ","
    do = "!"
    content = '主机%s发生%s告警%s请关注%s' % (ip, msg, dot, do)
    message = content.encode("GBK")
    response = send_message(user_phone, message)
    if 200 == response.status_code:
        print('与服务器连接c成功：', response.status_code)
    else:
        print('与服务器连接失败：', response.status_code)


if __name__ == '__main__':
    get_problem_message()