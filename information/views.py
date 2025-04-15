
# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .models import NHANVIEN
from .models import HOPDONG
from .models import BAOCAO
from .models import CUAHANGNHUONGQUYEN
from .models import BEN_NNQ
from .models import GOINHUONGQUYEN
from .models import LyLich
from .models import NGUOITHAN
from .models import KHO
from .models import PHIEUNHAP
from .models import HANG
from .models import CTPN
from .models import CTPX
from .models import BAOCAO
from .models import PHIEUXUAT
from .models import BANGXACTHUC
from information.form.forms import NhanVienForm
from information.form.forms import HopDongForm
from information.form.forms import CuaHangNhuongQuyenForm
from information.form.forms import BenNNQForm
from information.form.forms import GoiNhuongQuyenForm
from information.form.forms import LyLichForm
from information.form.forms import NguoiThanForm
from information.form.forms import KhoForm
from information.form.forms import PhieuNhapForm
from information.form.forms import PhieuXuatForm
from information.form.forms import HangForm
from information.form.forms import CTPNForm
from information.form.forms import CTPXForm
from information.form.forms import BaoCaoForm
from information.form.forms import BangXacThucForm



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

def delete_nhanvien(request,pk):
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

def delete_hopdong(request,pk):
    hopdong = get_object_or_404(HOPDONG, pk=pk)
    hopdong.delete()
    return redirect('hopdong_list')

#CUAHANGNHUONGQUYEN
def cuahang_list(request):
    cuahangs = CUAHANGNHUONGQUYEN.objects.all()
    return render(request, 'cuahang_list.html', {'cuahangs': cuahangs})

def add_cuahang(request):
    if request.method == 'POST':
        form = CuaHangNhuongQuyenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuahang_list')
    else:
        form = CuaHangNhuongQuyenForm()
    return render(request, 'add_cuahang.html', {'form': form})

def edit_cuahang(request, pk):
    cuahang = get_object_or_404(CUAHANGNHUONGQUYEN, pk=pk)
    if request.method == 'POST':
        form = CuaHangNhuongQuyenForm(request.POST, instance=cuahang)
        if form.is_valid():
            form.save()
            return redirect('cuahang_list')
    else:
        form = CuaHangNhuongQuyenForm(instance=cuahang)
    return render(request, 'edit_cuahang.html', {'form': form})

def delete_cuahang(request,pk):
    cuahang = get_object_or_404(CUAHANGNHUONGQUYEN, pk=pk)
    cuahang.delete()
    return redirect('cuahang_list')

#BENNNQ
def bennnq_list(request):
    bennnqs = BEN_NNQ.objects.all()
    return render(request, 'bennnq_list.html', {'bennnqs': bennnqs})

def add_bennnq(request):
    if request.method == 'POST':
        form = BenNNQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bennnq_list')
    else:
        form = BenNNQForm()
    return render(request, 'add_bennnq.html', {'form': form})

def edit_bennnq(request, pk):
    bennnq = get_object_or_404(BEN_NNQ, pk=pk)
    if request.method == 'POST':
        form = BenNNQForm(request.POST, instance=bennnq)
        if form.is_valid():
            form.save()
            return redirect('bennnq_list')
    else:
        form = BenNNQForm(instance=bennnq)
    return render(request, 'edit_bennnq.html', {'form': form})

def delete_bennnq(request,pk):
    bennnq = get_object_or_404(BEN_NNQ, pk=pk)
    bennnq.delete()
    return redirect('bennnq_list')

#goi
def goi_list(request):
    gois = GOINHUONGQUYEN.objects.all()
    return render(request, 'goi_list.html', {'gois': gois})

def add_goi(request):
    if request.method == 'POST':
        form = GoiNhuongQuyenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goi_list')
    else:
        form = GoiNhuongQuyenForm()
    return render(request, 'add_goi.html', {'form': form})

def edit_goi(request, pk):
    goi = get_object_or_404(GOINHUONGQUYEN, pk=pk)
    if request.method == 'POST':
        form = GoiNhuongQuyenForm(request.POST, instance=goi)
        if form.is_valid():
            form.save()
            return redirect('goi_list')
    else:
        form = GoiNhuongQuyenForm(instance=goi)
    return render(request, 'edit_goi.html', {'form': form})

def delete_goi(request,pk):
    goi = get_object_or_404(GOINHUONGQUYEN, pk=pk)
    goi.delete()
    return redirect('goi_list')

#LyLich
def lylich_list(request):
    lylichs = LyLich.objects.all()
    return render(request, 'lylich_list.html', {'lylichs': lylichs})

def add_lylich(request):
    if request.method == 'POST':
        form = LyLichForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lylich_list')
    else:
        form = LyLichForm()
    return render(request, 'add_lylich.html', {'form': form})

def edit_lylich(request, pk):
    lylich = get_object_or_404(LyLich, pk=pk)
    if request.method == 'POST':
        form = LyLichForm(request.POST, instance=lylich)
        if form.is_valid():
            form.save()
            return redirect('lylich_list')
    else:
        form = LyLichForm(instance=lylich)
    return render(request, 'edit_lylich.html', {'form': form})

def delete_lylich(request,pk):
    lylich = get_object_or_404(LyLich, pk=pk)
    lylich.delete()
    return redirect('lylich_list')

#NGUOITHAN
def nguoithan_list(request):
    nguoithans = NGUOITHAN.objects.all()
    return render(request, 'nguoithan_list.html', {'nguoithans': nguoithans})

def add_nguoithan(request):
    if request.method == 'POST':
        form = NguoiThanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nguoithan_list')
    else:
        form = NguoiThanForm()
    return render(request, 'add_nguoithan.html', {'form': form})

def edit_nguoithan(request, pk):
    nguoithan = get_object_or_404(NGUOITHAN, pk=pk)
    if request.method == 'POST':
        form = NguoiThanForm(request.POST, instance=nguoithan)
        if form.is_valid():
            form.save()
            return redirect('nguoithan_list')
    else:
        form = NguoiThanForm(instance=nguoithan)
    return render(request, 'edit_nguoithan.html', {'form': form})

def delete_nguoithan(request,pk):
    nguoithan = get_object_or_404(NGUOITHAN, pk=pk)
    nguoithan.delete()
    return redirect('nguoithan_list')

#KHO
def kho_list(request):
    khos = KHO.objects.all()
    return render(request, 'kho_list.html', {'khos': khos})

def add_kho(request):
    if request.method == 'POST':
        form = KhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kho_list')
    else:
        form = KhoForm()
    return render(request, 'add_kho.html', {'form': form})

def edit_kho(request, pk):
    kho = get_object_or_404(KHO, pk=pk)
    if request.method == 'POST':
        form = KhoForm(request.POST, instance=kho)
        if form.is_valid():
            form.save()
            return redirect('kho_list')
    else:
        form = KhoForm(instance=kho)
    return render(request, 'edit_kho.html', {'form': form})

def delete_kho(request,pk):
    kho = get_object_or_404(KHO, pk=pk)
    kho.delete()
    return redirect('kho_list')

#PHIEUNHAP
def phieunhap_list(request):
    phieunhaps = PHIEUNHAP.objects.all()
    return render(request, 'phieunhap_list.html', {'phieunhaps': phieunhaps})

def add_phieunhap(request):
    if request.method == 'POST':
        form = PhieuNhapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phieunhap_list')
    else:
        form = PhieuNhapForm()
    return render(request, 'add_phieunhap.html', {'form': form})

def edit_phieunhap(request, pk):
    phieunhap = get_object_or_404(PHIEUNHAP, pk=pk)
    if request.method == 'POST':
        form = PhieuNhapForm(request.POST, instance=phieunhap)
        if form.is_valid():
            form.save()
            return redirect('phieunhap_list')
    else:
        form = PhieuNhapForm(instance=phieunhap)
    return render(request, 'edit_phieunhap.html', {'form': form})

def delete_phieunhap(request,pk):
    phieunhap = get_object_or_404(PHIEUNHAP, pk=pk)
    phieunhap.delete()
    return redirect('phieunhap_list')

#PHIEUXUAT
def phieuxuat_list(request):
    phieuxuats = PHIEUXUAT.objects.all()
    return render(request, 'phieuxuat_list.html', {'phieuxuats': phieuxuats})

def add_phieuxuat(request):
    if request.method == 'POST':
        form = PhieuXuatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phieuxuat_list')
    else:
        form = PhieuXuatForm()
    return render(request, 'add_phieuxuat.html', {'form': form})

def edit_phieuxuat(request, pk):
    phieuxuat = get_object_or_404(PHIEUXUAT, pk=pk)
    if request.method == 'POST':
        form = PhieuXuatForm(request.POST, instance=phieuxuat)
        if form.is_valid():
            form.save()
            return redirect('phieuxuat_list')
    else:
        form = PhieuXuatForm(instance=phieuxuat)
    return render(request, 'edit_phieuxuat.html', {'form': form})

def delete_phieuxuat(request,pk):
    phieuxuat = get_object_or_404(PHIEUXUAT, pk=pk)
    phieuxuat.delete()
    return redirect('phieuxuat_list')

#HANG
def hang_list(request):
    hangs = HANG.objects.all()
    return render(request, 'hang_list.html', {'hangs': hangs})

def add_hang(request):
    if request.method == 'POST':
        form = HangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hang_list')
    else:
        form = HangForm()
    return render(request, 'add_hang.html', {'form': form})

def edit_hang(request, pk):
    hang = get_object_or_404(HANG, pk=pk)
    if request.method == 'POST':
        form = HangForm(request.POST, instance=hang)
        if form.is_valid():
            form.save()
            return redirect('hang_list')
    else:
        form = HangForm(instance=hang)
    return render(request, 'edit_hang.html', {'form': form})

def delete_hang(request,pk):
    hang = get_object_or_404(HANG, pk=pk)
    hang.delete()
    return redirect('hang_list')

#CTPN
def ctpn_list(request):
    ctpns = CTPN.objects.all()
    return render(request, 'ctpn_list.html', {'ctpns': ctpns})

def add_ctpn(request):
    if request.method == 'POST':
        form = CTPNForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ctpn_list')
    else:
        form = CTPNForm()
    return render(request, 'add_ctpn.html', {'form': form})

def edit_ctpn(request, pk):
    ctpn = get_object_or_404(CTPN, pk=pk)
    if request.method == 'POST':
        form = CTPNForm(request.POST, instance=ctpn)
        if form.is_valid():
            form.save()
            return redirect('ctpn_list')
    else:
        form = CTPNForm(instance=ctpn)
    return render(request, 'edit_ctpn.html', {'form': form})

def delete_ctpn(request,pk):
    ctpn = get_object_or_404(CTPN, pk=pk)
    ctpn.delete()
    return redirect('ctpn_list')

#CTPX
def ctpx_list(request):
    ctpxs = CTPX.objects.all()
    return render(request, 'ctpx_list.html', {'ctpxs': ctpxs})

def add_ctpx(request):
    if request.method == 'POST':
        form = CTPXForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ctpx_list')
    else:
        form = CTPXForm()
    return render(request, 'add_ctpx.html', {'form': form})

def edit_ctpx(request, pk):
    ctpx = get_object_or_404(CTPX, pk=pk)
    if request.method == 'POST':
        form = CTPXForm(request.POST, instance=ctpx)
        if form.is_valid():
            form.save()
            return redirect('ctpx_list')
    else:
        form = CTPXForm(instance=ctpx)
    return render(request, 'edit_ctpx.html', {'form': form})

def delete_ctpx(request,pk):
    ctpx = get_object_or_404(CTPX, pk=pk)
    ctpx.delete()
    return redirect('ctpx_list')


#BAOCAO
def baocao_list(request):
    baocaos = BAOCAO.objects.all()
    return render(request, 'baocao_list.html', {'baocaos': baocaos})

def add_baocao(request):
    if request.method == 'POST':
        form = BaoCaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baocao_list')
    else:
        form = BaoCaoForm()
    return render(request, 'add_baocao.html', {'form': form})

def edit_baocao(request, pk):
    baocao = get_object_or_404(BAOCAO, pk=pk)
    if request.method == 'POST':
        form = BaoCaoForm(request.POST, instance=baocao)
        if form.is_valid():
            form.save()
            return redirect('baocao_list')
    else:
        form = BaoCaoForm(instance=baocao)
    return render(request, 'edit_baocao.html', {'form': form})

def delete_baocao(request,pk):
    baocao = get_object_or_404(BAOCAO, pk=pk)
    baocao.delete()
    return redirect('baocao_list')

#BANGXACTHUC
def bangxacthuc_list(request):
    bangxacthucs = BANGXACTHUC.objects.all()
    return render(request, 'bangxacthuc_list.html', {'bangxacthucs': bangxacthucs})

def add_bangxacthuc(request):
    if request.method == 'POST':
        form = BangXacThucForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bangxacthuc_list')
    else:
        form =BangXacThucForm()
    return render(request, 'add_bangxacthuc.html', {'form': form})

def edit_bangxacthuc(request, pk):
    bangxacthuc = get_object_or_404(BANGXACTHUC, pk=pk)
    if request.method == 'POST':
        form = BangXacThucForm(request.POST, instance=bangxacthuc)
        if form.is_valid():
            form.save()
            return redirect('bangxacthuc_list')
    else:
        form = BangXacThucForm(instance=bangxacthuc)
    return render(request, 'edit_bangxacthuc.html', {'form': form})

def delete_bangxacthuc(request,pk):
    bangxacthuc = get_object_or_404(BANGXACTHUC, pk=pk)
    bangxacthuc.delete()
    return redirect('bangxacthuc_list')

#DASHBOARD




def dashboard_view(request):
    tong_cuahang = CUAHANGNHUONGQUYEN.MACH.count()
    tong_nhanvien = NHANVIEN.objects.count()

    

    context = {
        'tong_cuahang': tong_cuahang,
        'tong_nhanvien': tong_nhanvien,
    }

    return render(request, 'dashboard.html', context)
