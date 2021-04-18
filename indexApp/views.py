#coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *
from . import loginJudge
from pocManageApp.models import Plugin_db


def index(request):
    if request.session.get('uname'):
        return HttpResponseRedirect("/mainIndex")
    else:
        return render(request,'index_app/login.html')

#用户登录视图
def loginCheck(request):
    username = request.POST['username']
    password = request.POST['password']
    count=int(Users.objects.filter(username=username).filter(password=password).count())
    if count>0:
        request.session['uname'] = username
        request.session.set_expiry(0) #设置session过期时间为游览器关闭
    return JsonResponse({'count':count})


@loginJudge.login
def mainIndex(request):
    uname = request.session['uname']
    return render(request,'index_app/index.html',{'uname':uname})


@loginJudge.login
def mainShow(request):
    plu_count = Plugin_db.objects.count()
    return render(request,'index_app/main.html',{'plu_count':plu_count})


#退出登录视图
@loginJudge.login
def logout(request):
    request.session.clear()
    return HttpResponseRedirect("/")