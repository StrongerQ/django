# http://blog.sina.com.cn/s/blog_a73687bc0101csdh.html
from django.contrib import admin
from  blog.models import *

# Register your models here.
admin.site.register(Publish,)

admin.site.register(Author,)

@admin.register(Book)
class MyAdmin(admin.ModelAdmin): #继承自定制方法
    list_display = ('name','price','publish',)
    search_fields = ('name',) #通过列名查询
    list_filter = ('name',) #增加过滤器
    ordering = ('price',) #排序
    # fieldsets =[(None,{'fields':['name',],}),
    #         ('price information', {'fields': ['price',"publish",'author'],}),
    #     ]
# admin.site.register(Book,MyAdmin) #绑定自定制方法


