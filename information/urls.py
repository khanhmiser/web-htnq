from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_nhanvien, name='add_nhanvien'),
    path('employees/edit/<str:pk>/', views.edit_nhanvien, name='edit_nhanvien'),
    path('employees/delete/<str:pk>/', views.delete_nhanvien, name='delete_nhanvien'),
    path('hopdong/', views.hopdong_list, name='hopdong_list'),
    path('hopdong/add', views.add_hopdong, name='add_hopdong'),
    path('hopdong/edit/<str:pk>/', views.edit_hopdong, name='edit_hopdong'),
    path('hopdong/delete/<str:pk>/', views.delete_hopdong, name='delete_hopdong'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
]