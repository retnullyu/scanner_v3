# coding=utf-8

from indexApp import loginJudge
from django.shortcuts import render

@loginJudge.login
def dicodeShow(request):
    return render(request, "decode/decodeShow.html")
