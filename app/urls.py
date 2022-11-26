from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('change-status/<int:pk>/<str:status>', views.change_status, name="status"),
    path('delete/<int:pk>/', views.delete_todo, name="delete"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup_user, name="signup"),
    path('edit/<int:pk>/', views.edit_details, name="edit_details"),
    path('logout/', views.logout_user, name="logout"),
]
