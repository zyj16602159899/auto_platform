from django.urls import path
from projects import views

# 子路由配置
# 1. 每一个应用（模块）都会维护一个子路由
# 2. 跟主路由一样，也是从上到下匹配
# 3. 能匹配上，则执行path第二个参数指定的视图，匹配不上则抛出404异常
urlpatterns = [
    path('index/', views.index),
    # 如果为类视图，那么path第二个函数为类视图名.as_view()，必须要有括号
    path('', views.IndexView.as_view())
]