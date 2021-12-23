"""test_blogademy URL Configuration

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
from apiserver.views import RegistrationAPIView, LoginAPIView, ChannelListCreateEndpoint, Registration2APIView, Login2APIView

from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    path('channels', ChannelListCreateEndpoint.as_view()),
    re_path(r'^registration2/?$', Registration2APIView.as_view(), name='user_registration2'),
    re_path(r'^login2/?$', Login2APIView.as_view(), name='user_login2'),
]