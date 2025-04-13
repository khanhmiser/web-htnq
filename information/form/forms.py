from django import forms
from information.models import NHANVIEN
from information.models import HOPDONG



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

        