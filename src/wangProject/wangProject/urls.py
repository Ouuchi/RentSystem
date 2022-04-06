"""wangProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from wangapp import views

urlpatterns = [
    ### 自由职业者列表
    path('employee/list/', views.employee_list),
    path('employee/<int:nid>/edit/', views.employee_edit),
    path('employee/<int:nid>/delete/', views.employee_delete),
    path('employee/add/', views.employee_add),

    ### 客户列表
    path('customer/list/', views.customer_list),
    path('customer/<int:nid>/edit/', views.customer_edit),
    path('customer/<int:nid>/delete/', views.customer_delete),
    path('customer/add/', views.customer_add),

    ## 项目列表
    path('project/list/', views.project_list),
    path('project/add/', views.project_add),
    path('project/<int:nid>/edit/', views.project_edit),

    ## 合同列表
    path('contrast/list/', views.contrast_list),
    path('contrast/add/', views.contrast_add),
    path('contrast/<int:nid>/delete/', views.contrast_delete),

    ## 登录
    path('login/', views.login_page),
    ## 注销
    path('logout/', views.logout),

    ## 自由职业者个人时间表
    path('emp/selflist/', views.emp_selflist)

]
