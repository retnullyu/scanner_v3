# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from vulCheckApp.models import *
import json
from ctypes import *
import sys
def _args_encode(args_string):
    '''Encode by utf-8 in PY3.'''
    if sys.version_info >= (3, 0):
        args_string = args_string.encode('utf-8')
    return args_string

def vulRetu(request):
    return render(request,"vulCheck/vulInput.html")

def vulcheck_input(request):
    objList = {}
    objList['flag'] = request.POST.get("flag","") #判断用户是否开启模糊搜索
    objList['vul_type'] = request.POST.get("vul_type","") #web or server
    if request.POST.get("target",""):
        objList['target'] = request.POST.get("target","") #模糊搜索字符
    objList['IP_URL'] = request.POST.get("IP_URL","") #ip or url
    return render(request,"vulCheck/vulOutput.html",{'objList':objList})


def vulstart(request):
    #处理参数
    flag = request.POST['flag'].encode('utf-8')
    vul_type = request.POST['vul_type'].encode('utf-8')
    IP_URL = request.POST['IP_URL'].encode('utf-8')
    if flag.encode('utf-8') == "1":
        target = request.POST['target'].encode('utf-8')
    else:
        target = "".encode('utf-8')

    kunpeng = cdll.LoadLibrary(r'D:\pythonWork\djangoProject\vul_config\kunpeng_c.dll')

    # 定义出入参变量类型
    kunpeng.GetPlugins.restype = c_char_p
    kunpeng.Check.argtypes = [c_char_p]
    kunpeng.Check.restype = c_char_p
    kunpeng.SetConfig.argtypes = [c_char_p]
    kunpeng.GetVersion.restype = c_char_p
    # 配置信息
    config = {
        'timeout': 10,
        # 'aider': 'http://xxxx:8080', # 漏洞辅助验证接口，部分漏洞无法通过回显判断是否存在漏洞，可通过辅助验证接口进行判断。python -c'import socket,base64;exec(base64.b64decode("aGlzdG9yeSA9IFtdCndlYiA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsc29ja2V0LlNPQ0tfU1RSRUFNKQp3ZWIuYmluZCgoJzAuMC4wLjAnLDgwODgpKQp3ZWIubGlzdGVuKDEwKQp3aGlsZSBUcnVlOgogICAgdHJ5OgogICAgICAgIGNvbm4sYWRkciA9IHdlYi5hY2NlcHQoKQogICAgICAgIGRhdGEgPSBjb25uLnJlY3YoNDA5NikKICAgICAgICByZXFfbGluZSA9IGRhdGEuc3BsaXQoIlxyXG4iKVswXQogICAgICAgIGFjdGlvbiA9IHJlcV9saW5lLnNwbGl0KClbMV0uc3BsaXQoJy8nKVsxXQogICAgICAgIHJhbmtfc3RyID0gcmVxX2xpbmUuc3BsaXQoKVsxXS5zcGxpdCgnLycpWzJdCiAgICAgICAgaHRtbCA9ICJORVcwMCIKICAgICAgICBpZiBhY3Rpb24gPT0gImFkZCI6CiAgICAgICAgICAgIGhpc3RvcnkuYXBwZW5kKHJhbmtfc3RyKQogICAgICAgICAgICBwcmludCAiYWRkIityYW5rX3N0cgogICAgICAgIGVsaWYgYWN0aW9uID09ICJjaGVjayI6CiAgICAgICAgICAgIHByaW50ICJjaGVjayIrcmFua19zdHIKICAgICAgICAgICAgaWYgcmFua19zdHIgaW4gaGlzdG9yeToKICAgICAgICAgICAgICAgIGh0bWw9IlZVTDAwIgogICAgICAgICAgICAgICAgaGlzdG9yeS5yZW1vdmUocmFua19zdHIpCiAgICAgICAgcmF3ID0gIkhUVFAvMS4wIDIwMCBPS1xyXG5Db250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLThcclxuQ29udGVudC1MZW5ndGg6ICVkXHJcbkNvbm5lY3Rpb246IGNsb3NlXHJcblxyXG4lcyIgJShsZW4oaHRtbCksaHRtbCkKICAgICAgICBjb25uLnNlbmQocmF3KQogICAgICAgIGNvbm4uY2xvc2UoKQogICAgZXhjZXB0OnBhc3M="))' 在辅助验证机器上运行以上代码，填入http://IP:8088，不开启则留空。
        # 'http_proxy': 'http://xxxxx:1080',
        # 'pass_list':['xtest'] // 默认密码字典，不定义则使用硬编码在代码里的小字典
        # 'extra_plugin_path': '/home/test/plugin/', //除已编译好的插件（Go、JSON）外，可指定额外插件目录（仅支持JSON插件），指定后程序会周期读取加载插件
    }

    conf_args = json.dumps(config)
    kunpeng.SetConfig(_args_encode(conf_args))

    # 开启日志打印
    # kunpeng.ShowLog()

    # 扫描目标
    # with open("ip.txt") as fp:
    # print(item)
    task = {
        'type': vul_type,  # 目标类型web或者service
        # 'type': 'service',
        'netloc': IP_URL,
        'target': target
        #     "meta":{
        #     "system": "windows",  //操作系统，部分漏洞检测方法不同系统存在差异，提供给插件进行判断
        #     "pathlist":[], //目录路径URL列表，部分插件需要此类信息，例如列目录漏洞插件
        #     "filelist":[], //文件路径URL列表，部分插件需要此类信息，例如struts2漏洞相关插件
        #     "passlist":[] //自定义密码字典
        # } // 非必填
    }

    print(task)
    task = _args_encode(json.dumps(task))
    out = kunpeng.Check(task)
    j = json.loads(out)
    return JsonResponse({'data':j})

def index(request):
    return render(request, 'index/index.html')






