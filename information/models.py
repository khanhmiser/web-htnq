from django.db import models

class PHONGBAN(models.Model):
    MAPB = models.CharField(max_length=5,primary_key=True)
    TENPB = models.CharField(max_length=100,null=False)

    class Meta:
        db_table = 'PHONGBAN'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAPB},{self.TENPB}"

class NHANVIEN(models.Model):
    MANV = models.CharField(max_length=10, primary_key=True)
    MAQL = models.CharField(max_length=10, null=True, blank=True)  # Mã người quản lý (tham chiếu đến chính nhân viên)
    phongban = models.ForeignKey(
        PHONGBAN,
        to_field='MAPB',
        db_column='MAPB',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_nhanvien'
    )
    HOTEN = models.CharField(max_length=100,null=False)
    EMAIL = models.EmailField(max_length=100,null=False)
    SDT = models.CharField(max_length=10,null=False)
    NGAYSINH = models.DateField(null=False)
    HESOLUONG = models.IntegerField(null=False)
    NGAYVAOLAM = models.DateField(null=False)

    class Meta:
        db_table = 'NHANVIEN'
        managed = False
       
    def __str__(self):
        return f"{self.MANV},{self.MAQL}, {self.phongban.MAPB},{self.HOTEN}, {self.EMAIL}, {self.SDT}, {self.NGAYSINH}, {self.HESOLUONG}, {self.NGAYVAOLAM}"

class BANGCAP(models.Model):
    SOHIEUBANG = models.CharField(max_length=5,null=False)
    SOVAOSO = models.CharField(max_length=20,null=False)
    NGAYCAPBANG = models.DateTimeField(null=True)
    XEPLOAI = models.CharField(max_length=100, null=True)
    HINHTHUCDAOTAO = models.CharField(max_length=100, null=True)
    NGUOICAP = models.CharField(max_length=100, null=True)
    CHUYENNGANHDAOTAO = models.CharField(max_length=100, null=True)
    THOIGIANDAOTAO = models.DateTimeField(null=True)
    THOIGIANKETTHUCDAOTAO = models.DateTimeField(null=True)
    NOICAP = models.CharField(max_length=100, null=True)
    nhanvien = models.ForeignKey(
        NHANVIEN,
        to_field='MANV',
        db_column='MANV',  
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_bangcap'
    )

    class Meta:
        unique_together = ['SOHIEUBANG', 'SOVAOSO', 'nhanvien']  # Đảm bảo ba trường này kết hợp thành khóa chính duy nhất
        db_table = 'BANGCAP'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False  # Django không quản lý bảng này (không tự động tạo hay xóa bảng)

    def __str__(self):
        # Dùng f-string để hiển thị tất cả các trường trong đối tượng
        return f"{self.SOHIEUBANG}, {self.SOVAOSO},{self.nhanvien.MANV}, " \
               f"{self.NGAYCAPBANG}, {self.XEPLOAI},{self.HINHTHUCDAOTAO}, " \
               f" {self.NGUOICAP}, {self.CHUYENNGANHDAOTAO}, " \
               f"{self.THOIGIANDAOTAO}, {self.THOIGIANKETTHUCDAOTAO}, " \
               f"{self.NOICAP}"

class BEN_NNQ(models.Model):
    MANHUONGQUYEN = models.CharField(max_length=10, primary_key=True)
    HOTEN = models.CharField(max_length=100,null=False)
    SDT = models.CharField(max_length=10,null=False)
    EMAIL = models.CharField(max_length=100,null=False)
    DIACHI = models.CharField(max_length=200,null=False)

    class Meta:
        db_table = 'BEN_NNQ'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MANHUONGQUYEN}, {self.HOTEN}, {self.SDT}, {self.EMAIL}, {self.DIACHI}"

class GOINHUONGQUYEN(models.Model):
    MAGOI = models.CharField(max_length=20, primary_key=True)
    TENGOI = models.CharField(max_length=255,null=False)
    VONDAUTU = models.DecimalField(max_digits=15, decimal_places=4,null=False)
    MOTAGOI = models.TextField(null=False)

    class Meta:
        db_table = 'GOINHUONGQUYEN'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAGOI}, {self.TENGOI}, {self.VONDAUTU}, {self.MOTAGOI}"

class HOPDONG(models.Model):
    MAHD = models.CharField(max_length=20, primary_key=True)
    CHIPHITONG = models.DecimalField(max_digits=15, decimal_places=4,null=False)
    NGAYBATDAU = models.DateField(null=False)
    NGAYKETTHUC = models.DateField(null=False)
    goi = models.ForeignKey(
        GOINHUONGQUYEN,
        to_field='MAGOI',
        db_column='MAGOI',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_goi'
    )
    nhuongquyen = models.ForeignKey(
        BEN_NNQ,
        to_field='MANHUONGQUYEN',
        db_column='MANHUONGQUYEN',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_nhuongquyen'
    )

    class Meta:
        # Đảm bảo kết hợp MAHD và MANHUONGQUYEN làm khóa chính duy nhất
        unique_together = ('MAHD', 'nhuongquyen')
        db_table = 'HOPDONG'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAHD}, {self.CHIPHITONG}, {self.NGAYBATDAU}, {self.NGAYKETTHUC}, {self.nhuongquyen.MANHUONGQUYEN}, {self.goi.MAGOI}"
    
class CUAHANGNHUONGQUYEN(models.Model):
    MACH = models.CharField(max_length=10,unique=True,primary_key=True)
    DIACHI = models.CharField(max_length=200)
    NGAYKHAITRUONG = models.DateTimeField()
    MASOTHUE = models.CharField(max_length=15)
    nhuongquyen = models.ForeignKey(
    BEN_NNQ,
        to_field='MANHUONGQUYEN',
        db_column='MANHUONGQUYEN',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_nq'
    )
    hopdong = models.ForeignKey(
    HOPDONG,
        to_field='MAHD',
        db_column='MAHD',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_hd'
    )

    class Meta:
        # Đảm bảo MACH, MANHUONGQUYEN, MAHD là khóa chính kết hợp
        unique_together = ('MACH', 'nhuongquyen', 'hopdong')
        db_table = 'CUAHANGNHUONGQUYEN'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False
        
    def __str__(self):
        return f"{self.MACH}, {self.DIACHI}, {self.NGAYKHAITRUONG}, {self.MASOTHUE}, {self.nhuongquyen.MANHUONGQUYEN}, {self.hopdong.MAHD}"

class KHO(models.Model):
    MAKHO = models.CharField(max_length=20, primary_key=True)
    TENKHO = models.CharField(max_length=255)
    DIACHI = models.CharField(max_length=200)

    class Meta:
        db_table = 'KHO'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAKHO}, {self.TENKHO}, {self.DIACHI}"

class HANG(models.Model):
    MAHANG = models.CharField(max_length=20, primary_key=True)
    TENHANG = models.CharField(max_length=255,null=False)
    DONVIDOLUONG = models.CharField(max_length=50,null=False)
    GIANHAP = models.DecimalField(max_digits=15, decimal_places=2,null=False)
    GIABAN = models.DecimalField(max_digits=15, decimal_places=2,null=False)
    LOAIHANG = models.CharField(max_length=255,null=False)
    kho = models.ForeignKey(
    KHO,
        to_field='MAKHO',
        db_column='MAKHO',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_kho'
    )

    class Meta:
        db_table = 'HANG'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAHANG},{self.kho.MAKHO},{self.TENHANG}, {self.DONVIDOLUONG},{self.GIANHAP}, {self.GIABAN}, {self.LOAIHANG}"

class NGUOITHAN(models.Model):
    IDNT = models.IntegerField(primary_key=True)
    TENNT = models.CharField(max_length=100)
    QUANHE = models.CharField(max_length=200)
    SDTNT = models.CharField(max_length=10, null=True)
    nhanvien = models.ForeignKey(
        NHANVIEN,
        to_field='MANV',
        db_column='MANV',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='ds_nv'
    )
    class Meta:
        db_table = 'NGUOITHAN'
        managed = False  # Không quản lý bảng trong cơ sở dữ liệu

    def __str__(self):
        return f"{self.IDNT},{self.TENNT}, {self.QUANHE}, {self.SDTNT}, {self.nhanvien.MANV}"


class PHIEUNHAP(models.Model):
    MAPHIEUNHAP = models.CharField(max_length=10, primary_key=True,null=False)
    NGAYNHAP = models.DateTimeField(null=False)
    nhanvien = models.ForeignKey(
    NHANVIEN,
        to_field='MANV',
        db_column='MANV', 
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='phieunhap_nhanvien'
    )
    class Meta:
        indexes = [
            models.Index(fields=['nhanvien']),  # Tạo chỉ mục cho trường MANV
        ]
        db_table = 'PHIEUNHAP'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAPHIEUNHAP}, {self.nhanvien.MANV}, {self.NGAYNHAP}"

class LyLich(models.Model):
    STT = models.AutoField(primary_key=True)
    TrinhDoVanHoa = models.CharField(max_length=200, null=True, blank=True)
    DanToc = models.CharField(max_length=200, null=True, blank=True)
    TonGiao = models.CharField(max_length=200, null=True, blank=True)
    TrinhDoChuyenMon = models.CharField(max_length=200, null=True, blank=True)
    NoiThuongTru = models.CharField(max_length=200, null=True, blank=True)
    NoiTamTru = models.CharField(max_length=200, null=True, blank=True)
    NoiSinh = models.CharField(max_length=200, null=True, blank=True)
    nhanvien = models.ForeignKey(
    NHANVIEN,
        to_field='MANV',
        db_column='MANV',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_nv2'
    )

    class Meta:
        unique_together = ['STT', 'nhanvien']
        db_table = 'LyLich'
        managed = False

    def __str__(self):
        return f" {self.STT},  {self.nhanvien.MANV}, {self.TrinhDoVanHoa}," \
               f" {self.DanToc},  {self.TonGiao}, {self.TrinhDoChuyenMon}," \
               f" {self.NoiThuongTru}, {self.NoiTamTru},{self.NoiSinh}"

class PHIEUXUAT(models.Model):
    MAPHIEUXUAT = models.CharField(max_length=10, primary_key=True)
    NGAYXUAT = models.DateTimeField(null=False)
    THOIGIANNHAPLIEU = models.DateTimeField(null=False)
    TINHTRANGNHAPLIEU = models.IntegerField(null=False)
    cuahang = models.ForeignKey(
    CUAHANGNHUONGQUYEN,
        to_field='MACH',
        db_column='MACH',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_CH'
    )

    class Meta:
        indexes = [
            models.Index(fields=['cuahang']), 
        ]
        db_table = 'PHIEUXUAT'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAPHIEUXUAT}, {self.cuahang.MACH}, {self.NGAYXUAT}, {self.THOIGIANNHAPLIEU}, {self.TINHTRANGNHAPLIEU}"

class BANGXACTHUC(models.Model):
    MaXacThuc = models.CharField(max_length=15, primary_key=True)
    GhiChuXT = models.TextField(null=True, blank=True)
    TinhTrangXT = models.BooleanField()
    NgayXT = models.DateField(null=True, blank=True)
    nhanvien = models.ForeignKey(
    NHANVIEN,
        to_field='MANV',
        db_column='MANV',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_nv3'
    )
    class Meta:
        db_table = 'BANGXACTHUC'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MaXacThuc}, {self.nhanvien.MANV}, {self.GhiChuXT}, {self.TinhTrangXT}, {self.NgayXT}"

class BAOCAO(models.Model):
    MABAOCAO = models.CharField(max_length=10, primary_key=True)
    LOAIBAOCAO = models.CharField(max_length=100, null=True)
    NGAYBAOCAO = models.DateTimeField(null=True)
    NOIDUNGBAOCAO = models.TextField(null=True)
    DOANHTHU = models.FloatField(null=True)
    cuahang = models.ForeignKey(
    CUAHANGNHUONGQUYEN,
        to_field='MACH',
        db_column='MACH',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_cuahang'
    )
    xacthuc = models.ForeignKey(
        BANGXACTHUC,
        to_field='MaXacThuc',
        db_column='MaXacThuc',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_xacthuc'
    )
    
    class Meta:
        indexes = [
            models.Index(fields=['cuahang'], name='GUI_THONG_TIN_FK'),  # Tạo chỉ mục cho cột MACH
        ]
        db_table = 'BAOCAO'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MABAOCAO}, {self.xacthuc.MaXacThuc},{self.cuahang.MACH},{self.LOAIBAOCAO}, {self.NGAYBAOCAO}, {self.NOIDUNGBAOCAO}, {self.DOANHTHU}"

class CTPN(models.Model):
    MAPHIEUNHAP = models.CharField(max_length=10, primary_key=True)
    SOLUONGNHAP = models.IntegerField(null=False)
    DONGIANHAP = models.DecimalField(max_digits=15, decimal_places=2,null=False)
    hang = models.ForeignKey(
        HANG,
        to_field='MAHANG',
        db_column='MAHANG',  # Django sẽ hiểu là dùng MAPB từ bảng NHANVIEN
        on_delete=models.DO_NOTHING,  # Không can thiệp vào CSDL
        null=True,
        blank=True,
        related_name='ds_hang'
    )
    class Meta:
        unique_together = ('MAPHIEUNHAP', 'hang')  # Đảm bảo MAHANG và MAPHIEUNHAP kết hợp làm khóa chính duy nhất
        db_table = 'CTPN'  # Đảm bảo tên bảng trong cơ sở dữ liệu trùng với bảng thực tế
        managed = False

    def __str__(self):
        return f"{self.MAPHIEUNHAP}, {self.hang.MAHANG}, {self.SOLUONGNHAP}, {self.DONGIANHAP}"

