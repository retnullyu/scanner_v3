#coding=utf-8
from django.http import HttpResponseRedirect

#判断是否登录
def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.get('uname'):
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/')
    return login_fun