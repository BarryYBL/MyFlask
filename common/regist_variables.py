# encoding=utf-8
import re
from modles.variables import Variables
from common.method_request import MethodRequest
from app import db
from flask import session


def to_regist_variables(name, method, url, data, headers, regist_variable='', regular=''):
    response_body = MethodRequest().request_value(method, url, data, headers)
    user_id = session.get('user_id')
    if 'html' in response_body:
        response_body = '<xmp> %s </xmp>' % response_body
    # print('response_body:', response_body.encode('utf-8').decode('gbk'))
    if regist_variable:
        # 判断是否有注册变量和正则方法，有的话进行获取
        if regular:
            regist_variable_value = re.compile(regular).findall(response_body)
            if len(regist_variable_value) > 0:
                if Variables.query.filter(Variables.name == regist_variable).count() > 0:
                    print('%s 请求结束,存在此变量时：' % url,  Variables.query.filter(Variables.name == regist_variable).first())
                    Variables.query.filter(Variables.name == regist_variable).first().value = regist_variable_value[0]
                    db.session.commit()
                    return response_body, regist_variable_value[0]
                private_variable_value = regist_variable_value[0]
                private_variable = Variables(regist_variable, private_variable_value, is_private=1, user_id=user_id)
                db.session.add(private_variable)
                db.session.commit()
                return response_body, regist_variable_value[0]
            return response_body, '未成功解析报文 %s ' % response_body
        if Variables.query.filter(Variables.name == regist_variable).count() > 0:
            Variables.query.filter(Variables.name == regist_variable).first().value = response_body
            db.session.commit()
            return response_body, response_body
        private_variable_value = response_body
        # print('no regular：', regist_variable, private_variable_value)
        private_variable = Variables(regist_variable, private_variable_value, is_private=1, user_id=user_id)
        db.session.add(private_variable)
        db.session.commit()
        return response_body, response_body
    return response_body, '未注册变量'
