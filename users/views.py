
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
    #GET����ʱrequest.GET,POST����ʱrequest.POST���صĶ���Query�����������ֵ�
    username=request.GET.get("username")
    print("j"*10,username)
    password=request.GET.get("password")

    isUser=False
    if users.get(username):
        isUser=True
    if isUser:
        user=username
        #redirect�ض�����������ַ�ʽ��һ����ֱ��дurl��һ����дapp:urlname
        # return redirect( '/users/index/', {'current_time': user})
        return redirect( 'users:index', {'current_time': user})
    else:
        error="no user"
        print("y"*10)
        # return render(request, 'users/login.html', {"error":error})
        return render(request, 'users/login.html')


    # return redirect(request,'index.html',{'current_time':user})