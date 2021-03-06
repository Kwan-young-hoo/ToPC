"""apServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include
from rest_framework import routers
from apServer.server import views
from apServer.server.urls import custom_router


router = routers.DefaultRouter()
router.register(r'v1/devices', views.DeviceInfoViewSet)


'''
Define URL Patterns
'''

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^v1/configs/interfaces/(?P<ifname>[a-z]+\d*)/v4addr$', views.InterfaceV4AddrConfigView.as_view()),
]

urlpatterns += router.urls
urlpatterns += custom_router.urls

