from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.signin, name="signin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('list-all-college-owners', views.list_all_college_owners, name="list_college_owners"),
    path('approve-college-owners/<int:owner_id>', views.approve_college_owners, name="approve_college_owners"),
    path('list-all-colleges', views.list_all_colleges, name="list_colleges"),
    path('view-colleges-by-owner/<int:owner_id>', views.view_colleges_by_owner, name="view_colleges_by_owner"),
    path('approve-colleges/<int:college_id>', views.approve_colleges, name="approve_colleges"),
    path('settings/state', views.settings_state, name="settings_state"),
    path('settings/state/delete/<int:id>', views.settings_state_delete, name="settings_state_delete"),
    path('settings/city', views.settings_city, name="settings_city"),
    path('settings/city/delete/<int:id>', views.settings_city_delete, name="settings_city_delete"),
    path('settings/course-type', views.settings_course_type, name="settings_course_type"),
    path('settings/course-type/delete/<int:id>', views.settings_course_type_delete, name="settings_course_type_delete"),
    path('settings/course-stream', views.settings_course_stream, name="settings_course_stream"),
    path('settings/course-stream/delete/<int:id>', views.settings_course_stream_delete, name="settings_course_stream_delete"),
    path('add-course-types', views.add_course_type, name="add_course_type"),
    path('logout', views.logout, name='logout'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


