"""eduvy_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
#Super Admin
    path('admin2020/', include('super_admin.urls')),
#Collge Owners
    path('college-owners/', include('college_owners.urls')),
#Principal
    path('principal/', include('principal.urls')),
#Office_administrator
    path('office-administrator/', include('office_administrator.urls')),
#Teacher
    path('teacher/', include('teacher.urls')),
#Student
    path('student/', include('student.urls')),
#Common Pages
    path('', include('common_pages.urls')),
]
