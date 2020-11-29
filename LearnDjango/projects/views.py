from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.


def index(request):
    """
    函数视图
    :param request: 是HttpRequest对象，包含前端用户的所有请求信息
    :return: 必须返回一个HttpResponse对象或子对象
    """
    if request.method == 'GET':
        return HttpResponse("<h1>这是get请求内容</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>这是post请求内容</h1>")
    else:
        return HttpResponse("<h1>这是other请求内容</h1>")


# 类视图
class IndexView(View):
    """
    index主页类视图
    """
    def get(self, request):
        """get请求"""
        return HttpResponse("<h1>这是get请求内容</h1>")

    def post(self, request):
        """post请求"""
        return HttpResponse("<h1>这是post请求内容</h1>")

    def put(self, request):
        """post请求"""
        return HttpResponse("<h1>这是put请求内容</h1>")

    def delete(self, request):
        """post请求"""
        return HttpResponse("<h1>这是delete请求内容</h1>")