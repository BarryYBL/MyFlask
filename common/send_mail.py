from flask_mail import Message
from flask import render_template
from threading import Thread


def async_send_mail(mail, app, msg):
    # �� ȡ��ǰ�����������
    with app.app_context():
        mail.send(message=msg)  # Mail�ĳ�Ա����send����


def send_mail(subject, to_user_list, items, allocation, testcase_scene_list):
    from app import get_app_mail
    app, mail = get_app_mail()
    msg = Message(subject, recipients=to_user_list)
    msg.html = render_template("testcase_report/testcase_report_email.html", items=items, allocation=allocation,
                               testcase_scene_list=testcase_scene_list)
    send = Thread(target=async_send_mail, args=(mail, app, msg))  # ʵ����һ���̣߳�
    send.start()  # ��ʼ�߳�





