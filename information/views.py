
# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import NHANVIEN
from .models import HOPDONG
from .models import BAOCAO
from information.form.forms import NhanVienForm
from information.form.forms import HopDongForm

#login
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Sai tên đăng nhập hoặc mật khẩu.')

    return render(request, 'login.html') ## chỉnh lại trang xí

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')  # 👈 Nếu chưa login thì redirect về /
def dashboard(request):
    return render(request, 'dashboard.html')
#EMPLOYEE
@login_required(login_url='login')  #Nếu không đăng nhập, họ sẽ bị chuyển hướng về trang login (ở đây là 'login.html').
def employee_list(request):
    employees = NHANVIEN.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def baocao_list(request):
    baocao = BAOCAO.objects.all()
    return render(request,'baocao_list.html',{'baocao':baocao})

def add_nhanvien(request):
    if request.method == 'POST':
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = NhanVienForm()
    return render(request, 'add_nhanvien.html', {'form': form})

def edit_nhanvien(request, pk):
    nhanvien = get_object_or_404(NHANVIEN, pk=pk)
    if request.method == 'POST':
        form = NhanVienForm(request.POST, instance=nhanvien)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = NhanVienForm(instance=nhanvien)
    return render(request, 'edit_nhanvien.html', {'form': form})

def delete_nhanvien(pk):
    nhanvien = get_object_or_404(NHANVIEN, pk=pk)
    nhanvien.delete()
    return redirect('employee_list')

#HOPDONG
def hopdong_list(request):
    hopdongs = HOPDONG.objects.all()
    return render(request, 'hopdong_list.html', {'hopdongs': hopdongs})

def add_hopdong(request):
    if request.method == 'POST':
        form = HopDongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hopdong_list')
    else:
        form = HopDongForm()
    return render(request, 'add_hopdong.html', {'form': form})

def edit_hopdong(request, pk):
    hopdong = get_object_or_404(HOPDONG, pk=pk)
    if request.method == 'POST':
        form = HopDongForm(request.POST, instance=hopdong)
        if form.is_valid():
            form.save()
            return redirect('hopdong_list')
    else:
        form = HopDongForm(instance=hopdong)
    return render(request, 'edit_hopdong.html', {'form': form})

def delete_hopdong(pk):
    hopdong = get_object_or_404(HOPDONG, pk=pk)
    hopdong.delete()
    return redirect('hopdong_list')
# Create your views here.
