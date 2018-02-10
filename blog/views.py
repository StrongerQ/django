from django.shortcuts import render,HttpResponse,redirect
import datetime
from blog import models
from django.db.models import Avg,Min,Sum,Max,F,Q

# Create your views here.
def login(rq,world,name):
    username = '没人'
    num = 10
    # Kname = ''
    A = "<a href='#'>check</a>"
    times = datetime.datetime.now()
    if  rq.method=='POST':
        username = rq.POST.get('user')
        if rq.POST.get('user')=='rq':
            rq.session['is_login']=True
            return redirect("http://www.baidu.com")
    # return render(rq,"hello.html",{"name":world,'user':username})
    # list = [1,2,3,4]
    list = {'name':[1,2,3,4],"sex":345}
    return render(rq,"hello.html",locals())

def ins(rq):
    # obj = models.Book.objects.create(
    #                                     name='python',
    #                                     price=59,
    #                                     publish_id=1,
    #                                                 )
    # models.Book.objects.all().update(price=F('price')+20)#F查询到price的值(对一列数字操作)
    # obj=models.Book.objects.filter((Q(id__gt=3)|Q(name="花"))&(Q(publish__name='mianzhu')|~Q(name='wefwf')),name='花')[0]
    # obj=models.Book.objects.filter((Q(id__gt=3)|Q(publish__name='mianzhu')))[0]
    obj=models.Book.objects.filter((Q(id__gt=3)|Q(publish__name='mianzhu')))[0]
    #Q 封装关键字查询 非Q条件放在最后
    print(obj)
    return HttpResponse('成功')

def cha(rq):
    # obj = models.Book.objects.filter(publish__name__contains='m').values('name')
    obj = models.Book.objects.filter(name='花').values('publish__name')
    # obj = models.Publish.objects.filter(book__author__name__icontains='al').values('name')[0]['name']
    # print(obj)
    Avgprice = models.Book.objects.aggregate(Avg('price'),) #先聚合查询再操作
    fuzu = models.Book.objects.values('name').annotate(Sum('price'),) #分组查询再操作

    print(fuzu)

    return  HttpResponse('OK')

def index(rq):


    return render(rq,"index.html")


def ajax(rq):

    return HttpResponse("HELLO")


from django import views

class login(views.View):
    def get(self):
        return HttpResponse('OK')
    def post(self,rq):
        pass