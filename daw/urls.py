"""daw URL Configuration

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
from django.conf.urls import url, include
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

#from daw.daw.settings import STATIC_URL
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',landing, name="landing"),
    path('home/', home, name="home"),
    path('login/', login_usuario,name="login"),
    path('registro/', registro,name="registro"),
]


if settings.MEDIA_URL.startswith("/"):
    urlpatterns += [
        url(
            r'^{MEDIA_URL}(?P<path>.*)$'.format(MEDIA_URL=re.escape(settings.MEDIA_URL.lstrip('/'))),
            serve,
            {'document_root': settings.MEDIA_ROOT},
        ),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.STATIC_URL.startswith("/"):
    urlpatterns+= [
        url(
            r'^{STATIC_URL}(?P<path>.*)$'.format(STATIC_URL=re.escape(settings.STATIC_URL.lstrip('/'))),
            serve,
            {'document_root': settings.STATIC_ROOT},
        ),
    ]