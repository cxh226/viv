"""viv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path , include , re_path
from tasks import  views as tasks_views
from users import  views as  users_views
from django.conf.urls import url


urlpatterns = [

    path('index/', tasks_views.index),
    path('register/', users_views.register ),
    path('login/', users_views.login),
    path('logout/', users_views.logout),
    path('admin/', admin.site.urls),
    path('register/<id>/', users_views.register),  #需要带上级会员账号ID

    path('captcha', include('captcha.urls'))  #验证码

]
