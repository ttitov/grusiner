"""grusiner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from tripapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('i18n/', include('django.conf.urls.i18n')),
    path('travel/', v.travel),
    path('books/', v.books),
    path('guitars/', v.guitars),
]

urlpatterns += staticfiles_urlpatterns()