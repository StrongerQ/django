from django.shortcuts import render,HttpResponse,redirect
import datetime

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
            return redirect("http://www.baidu.com")
    # return render(rq,"hello.html",{"name":world,'user':username})
    # list = [1,2,3,4]
    list = {'name':[1,2,3,4],"sex":345}
    return render(rq,"hello.html",locals())