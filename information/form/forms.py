from django import forms
from information.models import NHANVIEN
from information.models import HOPDONG
from information.models import CUAHANGNHUONGQUYEN
from information.models import BEN_NNQ
from information.models import GOINHUONGQUYEN
from information.models import LyLich
from information.models import NGUOITHAN
from information.models import KHO
from information.models import PHIEUNHAP
from information.models import PHIEUXUAT
from information.models import HANG
from information.models import CTPN
from information.models import CTPX
from information.models import BAOCAO
from information.models import BANGXACTHUC



class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NHANVIEN
        fields = ['MANV', 'MAQL', 'phongban', 'HOTEN', 'EMAIL', 'SDT', 'NGAYSINH', 'HESOLUONG', 'NGAYVAOLAM']
        
        widgets = {
            'MANV': forms.TextInput(attrs={'class': 'form-control'}),
            'MAQL': forms.TextInput(attrs={'class': 'form-control'}),
            'phongban': forms.Select(attrs={'class': 'form-select'}),  # nếu là dropdown
            'HOTEN': forms.TextInput(attrs={'class': 'form-control'}),
            'EMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'SDT': forms.TextInput(attrs={'class': 'form-control'}),
            'NGAYSINH': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'HESOLUONG': forms.NumberInput(attrs={'class': 'form-control'}),
            'NGAYVAOLAM': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class HopDongForm(forms.ModelForm):
    class Meta:
        model = HOPDONG
        fields = '__all__'
        widgets = {
            'MAHD': forms.TextInput(attrs={'class': 'form-control'}),
            'CHIPHITONG': forms.NumberInput(attrs={'class': 'form-control'}),
            'NGAYBATDAU': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'NGAYKETTHUC': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'goi': forms.Select(attrs={'class': 'form-control'}),
            'nhuongquyen': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sử dụng label_from_instance để chỉ hiển thị MAGOI trong dropdown
        self.fields['goi'].label_from_instance = lambda obj: f"{obj.MAGOI} - {obj.TENGOI}"
        self.fields['nhuongquyen'].label_from_instance = lambda obj: obj.MANHUONGQUYEN

class CuaHangNhuongQuyenForm(forms.ModelForm):
    class Meta:
        model = CUAHANGNHUONGQUYEN
        fields = '__all__'
        widgets = {
            'MACH': forms.TextInput(attrs={'class': 'form-control'}),
            'DIACHI': forms.TextInput(attrs={'class': 'form-control'}),
            'NGAYKHAITRUONG': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'MASOTHUE': forms.TextInput(attrs={'class': 'form-control'}),
            'nhuongquyen': forms.Select(attrs={'class': 'form-control'}),
            'hopdong': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh hiển thị label trong dropdown nếu cần
        self.fields['nhuongquyen'].label_from_instance = lambda obj: f"{obj.MANHUONGQUYEN}"
        self.fields['hopdong'].label_from_instance = lambda obj: f"{obj.MAHD}"

class BenNNQForm(forms.ModelForm):
    class Meta:
        model = BEN_NNQ
        fields = '__all__'
        widgets = {
            'MANHUONGQUYEN': forms.TextInput(attrs={'class': 'form-control'}),
            'HOTEN': forms.TextInput(attrs={'class': 'form-control'}),
            'SDT': forms.TextInput(attrs={'class': 'form-control'}),
            'EMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'DIACHI': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GoiNhuongQuyenForm(forms.ModelForm):
    class Meta:
        model = GOINHUONGQUYEN
        fields = '__all__'
        widgets = {
            'MAGOI': forms.TextInput(attrs={'class': 'form-control'}),
            'TENGOI': forms.TextInput(attrs={'class': 'form-control'}),
            'VONDAUTU': forms.NumberInput(attrs={'class': 'form-control'}),
            'MOTAGOI': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LyLichForm(forms.ModelForm):
    class Meta:
        model = LyLich
        fields = '__all__'
        widgets = {
            'TrinhDoVanHoa': forms.TextInput(attrs={'class': 'form-control'}),
            'DanToc': forms.TextInput(attrs={'class': 'form-control'}),
            'TonGiao': forms.TextInput(attrs={'class': 'form-control'}),
            'TrinhDoChuyenMon': forms.TextInput(attrs={'class': 'form-control'}),
            'NoiThuongTru': forms.TextInput(attrs={'class': 'form-control'}),
            'NoiTamTru': forms.TextInput(attrs={'class': 'form-control'}),
            'NoiSinh': forms.TextInput(attrs={'class': 'form-control'}),
            'nhanvien': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hiển thị thông minh cho dropdown nhân viên
        self.fields['nhanvien'].label_from_instance = lambda obj: f"{obj.MANV} - {obj.HOTEN}"

class NguoiThanForm(forms.ModelForm):
    class Meta:
        model = NGUOITHAN
        fields = '__all__'
        widgets = {
            'IDNT': forms.TextInput(attrs={'class': 'form-control'}),
            'TENNT': forms.TextInput(attrs={'class': 'form-control'}),
            'QUANHE': forms.TextInput(attrs={'class': 'form-control'}),
            'SDTNT': forms.TextInput(attrs={'class': 'form-control'}),
            'nhanvien': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hiển thị chi tiết nhân viên trong dropdown
        self.fields['nhanvien'].label_from_instance = lambda obj: f"{obj.MANV} - {obj.HOTEN}"

class KhoForm(forms.ModelForm):
    class Meta:
        model = KHO
        fields = '__all__'
        widgets = {
            'MAKHO': forms.TextInput(attrs={'class': 'form-control'}),
            'TENKHO': forms.TextInput(attrs={'class': 'form-control'}),
            'DIACHI': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PhieuNhapForm(forms.ModelForm):
    class Meta:
        model = PHIEUNHAP
        fields = '__all__'
        widgets = {
            'MAPHIEUNHAP': forms.TextInput(attrs={'class': 'form-control'}),
            'NGAYNHAP': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'nhanvien': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho trường nhân viên
        self.fields['nhanvien'].label_from_instance = lambda obj: f"{obj.MANV} - {obj.HOTEN}"

class PhieuXuatForm(forms.ModelForm):
    class Meta:
        model = PHIEUXUAT
        fields = '__all__'
        widgets = {
            'MAPHIEUXUAT': forms.TextInput(attrs={'class': 'form-control'}),
            'NGAYXUAT': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 'class': 'form-control'
            }),
            'THOIGIANNHAPLIEU': forms.DateTimeInput(attrs={
                'type': 'datetime-local', 'class': 'form-control'
            }),
            'TINHTRANGNHAPLIEU': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuahang': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho cửa hàng nhượng quyền
        self.fields['cuahang'].label_from_instance = lambda obj: f"{obj.MACH}"

class HangForm(forms.ModelForm):
    class Meta:
        model = HANG
        fields = '__all__'
        widgets = {
            'MAHANG': forms.TextInput(attrs={'class': 'form-control'}),
            'TENHANG': forms.TextInput(attrs={'class': 'form-control'}),
            'DONVIDOLUONG': forms.TextInput(attrs={'class': 'form-control'}),
            'GIANHAP': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'GIABAN': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'LOAIHANG': forms.TextInput(attrs={'class': 'form-control'}),
            'kho': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Tùy chỉnh cách hiển thị kho trong dropdown
        self.fields['kho'].label_from_instance = lambda obj: f"{obj.MAKHO} - {obj.TENKHO}"

class CTPNForm(forms.ModelForm):
    class Meta:
        model = CTPN
        fields = '__all__'
        widgets = {
            'MAPHIEUNHAP': forms.TextInput(attrs={'class': 'form-control'}),
            'SOLUONGNHAP': forms.NumberInput(attrs={'class': 'form-control'}),
            'DONGIANHAP': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'hang': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho trường hang
        self.fields['hang'].label_from_instance = lambda obj: f"{obj.MAHANG} - {obj.TENHANG}"

class CTPXForm(forms.ModelForm):
    class Meta:
        model = CTPX
        fields = '__all__'
        widgets = {
            'MAPHIEUXUAT': forms.TextInput(attrs={'class': 'form-control'}),
            'SOLUONGXUAT': forms.NumberInput(attrs={'class': 'form-control'}),
            'DONGIAXUAT': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'DONVITINH': forms.TextInput(attrs={'class': 'form-control'}),
            'GIAMGIABAN': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'MAHANG': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho trường MAHANG (liên kết với bảng HANG)
        self.fields['MAHANG'].label_from_instance = lambda obj: f"{obj.MAHANG} - {obj.TENHANG}"

class BaoCaoForm(forms.ModelForm):
    class Meta:
        model = BAOCAO
        fields = '__all__'
        widgets = {
            'MABAOCAO': forms.TextInput(attrs={'class': 'form-control'}),
            'LOAIBAOCAO': forms.TextInput(attrs={'class': 'form-control'}),
            'NGAYBAOCAO': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'NOIDUNGBAOCAO': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'DOANHTHU': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cuahang': forms.Select(attrs={'class': 'form-control'}),
            'xacthuc': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho các trường foreign key
        self.fields['cuahang'].label_from_instance = lambda obj: f"{obj.MACH}"  # Đảm bảo rằng TENCH là trường hợp đúng
        self.fields['xacthuc'].label_from_instance = lambda obj: f"{obj.MaXacThuc} "

class BangXacThucForm(forms.ModelForm):
    class Meta:
        model = BANGXACTHUC
        fields = '__all__'
        widgets = {
            'MaXacThuc': forms.TextInput(attrs={'class': 'form-control'}),
            'GhiChuXT': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'TinhTrangXT': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'NgayXT': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nhanvien': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tùy chỉnh label hiển thị cho trường nhanvien
        self.fields['nhanvien'].label_from_instance = lambda obj: f"{obj.MANV} - {obj.HOTEN}"