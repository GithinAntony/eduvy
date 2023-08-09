from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.signin, name="signin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('list-courses', views.list_courses, name="list_courses"),
    path('add-courses', views.add_courses, name="add_courses"),
    path('delete-courses/<int:id>', views.delete_courses, name="add_courses"),
    path('add-admission/<int:id>', views.add_admission, name="add_admission"),
    path('logout', views.logout, name='logout'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


