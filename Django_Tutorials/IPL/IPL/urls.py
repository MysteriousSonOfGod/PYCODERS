"""IPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view=get_swagger_view(title='ravi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CSK/', include('CSK.urls')),
    path('DD/', include('DD.urls')),
    path('KIXP/', include('KIXP.urls')),
    path('KKR/', include('KKR.urls')),
    path('MI/', include('MI.urls')),
    path('RCB/', include('RCB.urls')),
    path('RR/', include('RR.urls')),
    path('SRH/', include('SRH.urls')),
    path('',schema_view),
]
