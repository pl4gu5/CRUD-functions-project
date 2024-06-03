from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name=""),
    path('register', views.Register, name="register"),
    path('login', views.My_Login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.create_record, name="create-record"),
    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('record/<int:pk>', views.single_record, name="view-record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    path('create-project', views.create_project, name="create-project"),
    path('update-project/<int:pk>', views.update_project, name="update-project"),
    path('project/<int:pk>', views.single_project, name="view-project"),
    path('delete-project/<int:pk>', views.delete_project, name="delete-project"),

]