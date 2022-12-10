
from django.shortcuts import render,redirect
from django.http import HttpResponse
import time
# Create your views here.
def index(request):
    # return HttpResponse('HELLO WORLD')
    return render(request,'index.html',{'current_time':time.time()})

def login(request):
    # return HttpResponse('HELLO WORLD')
    return render(request,'login.html',{'current_time000':time.time()})

def valid_login(request):
    # return HttpResponse('HELLO WORLD')

    users={"1":"hhh"}
    #GET请求时request.GET,POST请求时request.POST返回的都是Query对象，类似于字典
    username=request.GET.get("username")
    print("j"*10,username)
    password=request.GET.get("password")

    isUser=False
    if users.get(username):
        isUser=True
    if isUser:
        user=username
        #redirect重定向可以有两种方式，一个是直接写url·一个是写app:urlname
        # return redirect( '/users/index/', {'current_time': user})
        return redirect( 'users:index', {'current_time': user})
    else:
        error="no user"
        print("y"*10)
        # return render(request, 'users/login.html', {"error":error})
        return render(request, 'users/login.html')


    # return redirect(request,'index.html',{'current_time':user})