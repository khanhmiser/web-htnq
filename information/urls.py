from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #NHÂN VIÊN
    path('dashboard/employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_nhanvien, name='add_nhanvien'),
    path('employees/edit/<str:pk>/', views.edit_nhanvien, name='edit_nhanvien'),
    path('employees/delete/<str:pk>/', views.delete_nhanvien, name='delete_nhanvien'),
    # HỢP ĐỒNG
    path('dashboard/hopdong/', views.hopdong_list, name='hopdong_list'),
    path('hopdong/add', views.add_hopdong, name='add_hopdong'),
    path('hopdong/edit/<str:pk>/', views.edit_hopdong, name='edit_hopdong'),
    path('hopdong/delete/<str:pk>/', views.delete_hopdong, name='delete_hopdong'),
    #CỬA HÀNG
    path('dashboard/cuahang/', views.cuahang_list, name='cuahang_list'),
    path('cuahang/add', views.add_cuahang, name='add_cuahang'),
    path('cuahang/edit/<str:pk>/', views.edit_cuahang, name='edit_cuahang'),
    path('cuahang/delete/<str:pk>/', views.delete_cuahang, name='delete_cuahang'),
    #BEN NNQ
    path('dashboard/bennnq/', views.bennnq_list, name='bennnq_list'),
    path('bennnq/add', views.add_bennnq, name='add_bennnq'),
    path('bennnq/edit/<str:pk>/', views.edit_bennnq, name='edit_bennnq'),
    path('bennnq/delete/<str:pk>/', views.delete_bennnq, name='delete_bennnq'),
    # GOI
    path('dashboard/goi/', views.goi_list, name='goi_list'),
    path('goi/add', views.add_goi, name='add_goi'),
    path('goi/edit/<str:pk>/', views.edit_goi, name='edit_goi'),
    path('goi/delete/<str:pk>/', views.delete_goi, name='delete_goi'),
    #LYLICH
    path('dashboard/lylich/', views.lylich_list, name='lylich_list'),
    path('lylich/add', views.add_lylich, name='add_lylich'),
    path('lylich/edit/<str:pk>/', views.edit_lylich, name='edit_lylich'),
    path('lylich/delete/<str:pk>/', views.delete_lylich, name='delete_lylich'),
    #NGUOITHAN
    path('dashboard/nguoithan/', views.nguoithan_list, name='nguoithan_list'),
    path('nguoithan/add', views.add_nguoithan, name='add_nguoithan'),
    path('nguoithan/edit/<str:pk>/', views.edit_nguoithan, name='edit_nguoithan'),
    path('nguoithan/delete/<str:pk>/', views.delete_nguoithan, name='delete_nguoithan'),
    #KHO
    path('dashboard/kho/', views.kho_list, name='kho_list'),
    path('kho/add', views.add_kho, name='add_kho'),
    path('kho/edit/<str:pk>/', views.edit_kho, name='edit_kho'),
    path('kho/delete/<str:pk>/', views.delete_kho, name='delete_kho'),
    #PHIEUNHAP
    path('dashboard/phieunhap/', views.phieunhap_list, name='phieunhap_list'),
    path('phieunhap/add', views.add_phieunhap, name='add_phieunhap'),
    path('phieunhap/edit/<str:pk>/', views.edit_phieunhap, name='edit_phieunhap'),
    path('phieunhap/delete/<str:pk>/', views.delete_phieunhap, name='delete_phieunhap'),
    #PHIEUXUAT
    path('dashboard/phieuxuat/', views.phieuxuat_list, name='phieuxuat_list'),
    path('phieuxuat/add', views.add_phieuxuat, name='add_phieuxuat'),
    path('phieuxuat/edit/<str:pk>/', views.edit_phieuxuat, name='edit_phieuxuat'),
    path('phieuxuat/delete/<str:pk>/', views.delete_phieuxuat, name='delete_phieuxuat'),
    #HANG
    path('dashboard/hang/', views.hang_list, name='hang_list'),
    path('hang/add', views.add_hang, name='add_hang'),
    path('hang/edit/<str:pk>/', views.edit_hang, name='edit_hang'),
    path('hang/delete/<str:pk>/', views.delete_hang, name='delete_hang'),
    #CTPN
    path('dashboard/ctpn/', views.ctpn_list, name='ctpn_list'),
    path('ctpn/add', views.add_ctpn, name='add_ctpn'),
    path('ctpn/edit/<str:pk>/', views.edit_ctpn, name='edit_ctpn'),
    path('ctpn/delete/<str:pk>/', views.delete_ctpn, name='delete_ctpn'),
    #CTPX
    path('dashboard/ctpx/', views.ctpx_list, name='ctpx_list'),
    path('ctpx/add', views.add_ctpx, name='add_ctpx'),
    path('ctpx/edit/<str:pk>/', views.edit_ctpx, name='edit_ctpx'),
    path('ctpx/delete/<str:pk>/', views.delete_ctpx, name='delete_ctpx'),
    #BAOCAO
    path('dashboard/baocao/', views.baocao_list, name='baocao_list'),
    path('baocao/add', views.add_baocao, name='add_baocao'),
    path('baocao/edit/<str:pk>/', views.edit_baocao, name='edit_baocao'),
    path('baocao/delete/<str:pk>/', views.delete_baocao, name='delete_baocao'),
    #BANGXACTHUC
    path('dashboard/bangxacthuc/', views.bangxacthuc_list, name='bangxacthuc_list'),
    path('bangxacthuc/add', views.add_bangxacthuc, name='add_bangxacthuc'),
    path('bangxacthuc/edit/<str:pk>/', views.edit_bangxacthuc, name='edit_bangxacthuc'),
    path('bangxacthuc/delete/<str:pk>/', views.delete_bangxacthuc, name='delete_bangxacthuc'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
]