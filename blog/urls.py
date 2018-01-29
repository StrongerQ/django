#email: strongeren@163.com
#_autor: smallqiang
from blog import views
from django.urls import path,re_path
urlpatterns = [
    re_path('index/(?P<world>\w+)/(?P<name>\w+)/$',views.login,name='woqu'),
    re_path('cha/',views.cha),
    re_path('ins/',views.ins),

    ]
