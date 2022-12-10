# -*- coding=utf-8 -*-
# @Time: 2022/12/10 19:15
# @Author: John
# @File: urls.py
# @Software: PyCharm
from django.urls import path
from users import views

app_name='users'
urlpatterns = [

    path('index/', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('valid_login/', views.valid_login,name='login'),
]