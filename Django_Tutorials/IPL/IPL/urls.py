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

schema_view=get_swagger_view(title='IPL')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CSK/', include('CSK.urls')),
    path('DD/', include('DD.urls')),
    path('KIXP/', include('DD.urls')),
    path('KKR/', include('DD.urls')),
    path('MI/', include('DD.urls')),
    path('RCB/', include('DD.urls')),
    path('RR/', include('DD.urls')),
    path('SRH/', include('DD.urls')),
    path('',schema_view),
]
