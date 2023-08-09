from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.signin, name="signin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('faculty-hierarchy', views.faculty_hierarchy, name="faculty_hierarchy"),
    path('user-faculty-approve/<int:user_id>', views.faculty_approve, name="faculty_approve"),
    path('user-teacher-approve/<int:user_id>', views.teacher_approve, name="teacher_approve"),
    path('logout', views.logout, name='logout'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


