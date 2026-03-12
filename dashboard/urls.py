
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('dashboard',views.creator_dashboard,name="dashboard"),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('register/', views.register, name='register'),
    path('add-video/', views.add_video, name='add_video'),
    path('edit-video/<int:pk>/', views.edit_video, name='edit_video'),
    path('delete-video/<int:pk>/', views.delete_video, name='delete_video'),
    path('video/<int:pk>/resources/', views.manage_resources, name='manage_resources'),
]
