"""employee URL Configuration

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
from django.conf import settings
from .views import *
from .views import employee_form
from .views import insert

urlpatterns = [
    path('list/', employee_list, name='list'),  # get request for retrieve and display records
    path('', insert, name='insert'),  # get and post request for insert operation
    path('<int:id>/', employee_form, name='update'),  # get and post request for update operation
    path('delete/<int:id>', employee_delete, name='delete')

]
