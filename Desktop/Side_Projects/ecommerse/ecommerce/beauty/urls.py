"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from beauty import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Handles '/beauty/index/'
    path('about/', views.about, name='about'),
    path('dry/', views.about, name='dry'),
    path('oily/', views.about, name='oily'),
    path('combination/', views.about, name='combination'),
    path('normal/', views.about, name='normal'),
    path('daraja/stk_push', views.stk_push_callback, name='stk_push_callback'),
]


