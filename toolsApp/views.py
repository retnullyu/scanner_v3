# coding=utf-8

from django.shortcuts import render
from django.http import *
from indexApp import loginJudge
from lib import portScan, dirScan
import time
import IPy


@loginJudge.login
def portRetu(request):
    return render(request, "tools_app/portReady.html")


@loginJudge.login
def portReady(request):
    objList = {}
    objList['ipType'] = request.POST.get("ipType", "")
    objList['ips'] = request.POST.get("ips", "")
    objList['threadSize'] = request.POST.get("threadSize", "")
    objList['portType'] = request.POST.get("portType", "")
    objList['portNumber'] = request.POST.get("portNumber", "")
    return render(request, "tools_app/portShow.html", {'objList': objList})


# 端口扫描操作
@loginJudge.login
def portStart(request):
    # 处理参数
    ipType = request.POST['ipType']
    ips = request.POST['ips']
    threadSize = request.POST['threadSize']
    portType = request.POST['portType']
    portNumber = request.POST['portNumber']

    ipList = []
    if ipType == "1":
        ipList.append(ips)
    else:
        ipList = IPy.IP(ips)

    portList = []

    if portType == "1":
        for p in xrange(1, 65536):
            portList.append(p)
    else:
        portList = portNumber.split(",")

    # 将ip和端口整合到列表中
    endList = []
    for ip in ipList:
        for port in portList:
            endList.append((ip, port))

    # 开始扫描
    p = portScan.PortScan(threadSize, endList)
    messList = p.run()

    return JsonResponse({'data': messList, 'ipType': ipType})


@loginJudge.login
def dirRetu(request):
    return render(request, "tools_app/dirReady.html")


@loginJudge.login
def dirReady(request):
    import json
    objList = {}
    objList['domain'] = request.POST.get("domain", "")
    objList['threadSize'] = request.POST.get("threadSize", "")
    objList['isRecursion'] = request.POST.get("isRecursion", "-1")
    objList['isKeywords'] = request.POST.get("isKeywords", "")
    objList['keywords'] = request.POST.get("keywords", "")
    objList['dicts'] = request.POST.getlist("dicts", "")
    objList['dicts'] = json.dumps(objList['dicts'])
    objList['url_status'] = request.POST.getlist("url_status", "")
    objList['url_status'] = json.dumps(objList['url_status'])
    return render(request, "tools_app/dirShow.html", {'objList': objList})


# 目录扫描操作
@loginJudge.login
def dirStart(request):
    try:
        domain = request.POST["domain"]
        threadSize = request.POST["threadSize"]
        isRecursion = request.POST["isRecursion"]
        isKeywords = request.POST["isKeywords"]
        keywords = request.POST["keywords"]
        dicts = request.POST["dicts"]
        url_status = request.POST["url_status"]

        # 因为传递列表的问题，接收的是字符串，需要做下处理
        dicts = dicts.replace('"', "")
        dicts = dicts.replace('[', "")
        dicts = dicts.replace(']', "")
        dicts = dicts.replace(' ', "")
        dicts_list = dicts.split(",")

        url_status = url_status.replace('"', "")
        url_status = url_status.replace('[', "")
        url_status = url_status.replace(']', "")
        url_status = url_status.replace(' ', "")
        url_status_list = url_status.split(",")

        # 开始扫描
        d = dirScan.DirScan(domain, threadSize, isRecursion, isKeywords, keywords, dicts_list, url_status_list)
        mess_list = d.run()
    except Exception, e:
        print e

    return JsonResponse({'data': mess_list})



