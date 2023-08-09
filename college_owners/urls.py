from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.signin, name="signin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('list-college', views.list_college, name="list_college"),
    path('add-college', views.add_college, name="add_college"),
    path('user-hierarchy/<int:college_id>', views.user_hierarchy, name="user_hierarchy"),
    path('user-principal-approve/<int:college_id>/<int:user_id>', views.principal_approve, name="principal_approve"),

    path('logout', views.logout, name='logout'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


