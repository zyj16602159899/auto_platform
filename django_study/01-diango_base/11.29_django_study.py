"""
django的特点：
提供创建项目工程自动化工具
数据库ORM支持
模板
表单
Admin管理站点
文件管理
认证权限
session机制
缓存
"""

"""
MTV框架模式
（1）模型 Model  
数据存取层，处理与数据相关的所有事物
Django默认db.sqlite3，我们也可以用mysql, oracle
（2）视图 Views   
表现层，接收请求，进行业务处理，返回响应
如何在页面中显示
（3）模板 Template
业务逻辑层
模型和模板的桥梁，负责构造要返回的html页面
"""

"""
1.安装django
命令：pip install django==2.2

2.创建项目
命令：django-admin startproject 项目名

3.运行项目
命令：python manage.py runserver
或者：python manage.py runserver ip:port
"""

"""
项目结构：
LearnDjango/    项目根目录
manage.py       以多种方式与django项目交互的命令行工具
LearnDjango/    与项目根目录同名，项目相关的包
LearnDjango/settings.py     项目全局配置文件
LearnDjango/urls.py         声明的全局url路由表
LearnDjango/wsgi.py         兼容WSGI协议的web服务器入口文件
"""

"""
修改语言为中文
LANGUAGE_CODE = 'zh-hans'
修改时区为上海
TIME_ZONE = 'Asia/Shanghai'
"""

"""
创建子应用（app）
1.定义：
如果有一些业务功能模块，如何做到复用？
    将工程项目拆分为不同的子功能模块---以子应用的形式存在
    各功能模块之间可以保持相对的独立
    可以将该模块代码整体复制过去
    
    App可以理解为一个应用，一个项目下可以有多个app。
    一个项目会有很多个模块，每个模块对应一个应用，每个应用完成一个特定的功能。

2.命令：python manage.py startapp 子应用名

3.子应用结构：
migrations文件夹：用于存放数据库迁移历史记录的目录
__init__.py文件：表示目录是一个python模块
admin.py文件： 网站后台管理站点配置相关的文件
apps.py文件：  用于配置当前子应用相关信息的文件
models.py文件：写和数据库相关的内容
tests.py文件： 用于编写单元测试
views.py文件： 定义处理函数，视图函数

4.注册子应用
在settings.py文件中的INSTALLED_APPS添加创建的应用（app）名称
"""

"""
视图函数：
在views.py文件中定义视图函数
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
HttpResponse：返回html格式的数据使用
JsonResponse：返回json对象的数据使用
render：使用render渲染html页面，即return render(request, '文件名.html')
"""

"""
1.全局路由配置：
在urls.py文件中配置访问路径（也就是路由配置）
注意：Path是访问的绝对路径，url支持正则匹配，因此一般推荐url配置路径
导入url：from django.conf.urls import url
使用url配置路径：一般用^开头，/$结尾，引号前面加r

2.子路由配置
假如项目有多个子应用，可在每个子应用结构内都创建一个urls.py文件，每一个应用（模块）都维护一个子路由
和全局路由配置，urlpatterns为固定名称的列表，且列表中的一个元素就代表一条路由

3.使用：
全局路由配置的urls.py文件中，导入include：from django.urls import include
在列表中添加一条数据：path('子应用名/', include('子应用名.urls'))
之后就只需要在子路由中进行path的添加和修改即可
"""

"""
templates模板
模板可放在项目根目录下，或放在app下都可以，名称固定为【templates】
在settings.py文件下的TEMPLATES配置模板路径：'DIRS': [os.path.join(BASE_DIR, 'templates')]
"""

"""

"""