
INSERT INTO PHONGBAN (MAPB, TENPB)
VALUES
  ('PB001', 'Quản lý kho'),
  ('PB002', 'Kế toán'),
  ('PB003', 'Kiểm định chất lượng');
  
INSERT INTO KHO (MAKHO, TENKHO, DIACHI)
VALUES
 ('K01', 'Kho Hàng Miền Nam', '123 đường Võ Thị Sáu, Quận 1, TP HCM'),
('K02', 'Kho Hàng Miền Bắc', '56 đường Tôn Đức Thắng, Quan Ba Đình, Hà Nội'),
('K03', 'Kho Hàng Miền Trung', '32 đường Bạch Đằng, Quan Hải Châu, Đà nẵng'),
('K04', 'Kho Hàng Miền Tây', '258 đường Nam Kỳ Khởi Nghĩa, TP Mỹ Tho, Tiền Giang'),
('K05', 'Kho Hàng Biên Giới', '369 đường Ly Thái Độ, TP Lạng Sơn');

INSERT INTO BEN_NNQ (MANHUONGQUYEN, HOTEN, SDT, EMAIL, DIACHI)
VALUES
('MNQ01', 'Pham Van Binh', '0913456789', 'binh.pham@example.com', '12 Duong Tan Son Nhi, Quan Tan Phu, TP.HCM'),
('MNQ02', 'Nguyen Thi Cam', '0923456789', 'cam.nguyen@example.com', '34 Duong Cao Thang, Quan 3, TP.HCM'),
('MNQ03', 'Tran Van Dat', '0933456789', 'dat.tran@example.com', '56 Duong Nguyen Van Linh, Quan 7, TP.HCM'),
('MNQ04', 'Le Thi Hoa', '0943456789', 'hoa.le@example.com', '78 Duong Le Quang Dinh, Quan Binh Thanh, TP.HCM'),
('MNQ05', 'Do Minh Hieu', '0953456789', 'hieu.do@example.com', '90 Duong Kha Van Can, Quan Thu Duc, TP.HCM'),
('MNQ06', 'Bui Thi Huong', '0963456789', 'huong.bui@example.com', '112 Duong Xo Viet Nghe Tinh, Quan Binh Thanh, TP.HCM'),
('MNQ07', 'Nguyen Van Hai', '0973456789', 'hai.nguyen@example.com', '134 Duong Cong Hoa, Quan Tan Binh, TP.HCM'),
('MNQ08', 'Phan Quang Khai', '0983456789', 'khai.phan@example.com', '156 Duong Phan Dang Luu, Quan Phu Nhuan, TP.HCM'),
('MNQ09', 'Ly Thi Kim', '0993456789', 'kim.ly@example.com', '178 Duong Ba Thang Hai, Quan 10, TP.HCM'),
('MNQ10', 'Dang Van Lam', '0914567890', 'lam.dang@example.com', '200 Duong Dien Bien Phu, Quan 3, TP.HCM'),
('MNQ11', 'Nguyen Thi Loan', '0924567890', 'loan.nguyen@example.com', '222 Duong Le Van Sy, Quan 3, TP.HCM'),
('MNQ12', 'Tran Minh Long', '0934567890', 'long.tran@example.com', '244 Duong Hoang Dieu, Quan 4, TP.HCM'),
('MNQ13', 'Vu Quang Loc', '0944567890', 'loc.vu@example.com', '266 Duong Truong Sa, Quan Phu Nhuan, TP.HCM'),
('MNQ14', 'Nguyen Van Manh', '0954567890', 'manh.nguyen@example.com', '288 Duong Pham Van Dong, Quan Thu Duc, TP.HCM'),
('MNQ15', 'Hoang Thi Minh', '0964567890', 'minh.hoang@example.com', '310 Duong Nguyen Van Qua, Quan Go Vap, TP.HCM');

INSERT INTO GOINHUONGQUYEN (MAGOI, TENGOI, VONDAUTU, MOTAGOI)
VALUES
  ('GQ01', 'Gói Hưởng Quyền Cơ Bản', 1000000.0000, 'Gói cơ bản cung cấp các dịch vụ thiết yếu, hỗ trợ quyền lợi cơ bản cho người tham gia.'),
  ('GQ02', 'Gói Hưởng Quyền Nâng Cao', 2500000.0000, 'Gói nâng cao dành cho khách hàng cần nhiều quyền lợi hơn, bao gồm hỗ trợ ưu đãi và dịch vụ chăm sóc chuyên sâu.'),
  ('GQ03', 'Gói Hưởng Quyền Doanh Nghiệp', 5000000.0000, 'Gói doanh nghiệp thiết kế riêng cho các công ty, cung cấp các quyền lợi ưu việt và hỗ trợ tài chính tối ưu.'),
  ('GQ04', 'Gói Hưởng Quyền Cá Nhân', 1500000.0000, 'Gói cá nhân với mức đầu tư vừa phải, mang lại sự linh hoạt và nhiều lựa chọn quyền lợi phù hợp.'),
  ('GQ05', 'Gói Hưởng Quyền Cao Cấp', 10000000.0000, 'Gói cao cấp dành cho khách hàng VIP, bao gồm các dịch vụ tư vấn chuyên nghiệp, quyền lợi ưu đãi đặc biệt và hỗ trợ toàn diện.');

INSERT INTO NHANVIEN (MANV, NHA_MANV, MAPB, HOTEN, EMAIL, SDT, NGAYSINH, HESOLUONG, NGAYVAOLAM)
VALUES
  ('NV001', NULL, 'PB001', 'Nguyễn Kho A', 'khoa@example.com', '0900000001', '1985-01-01', 3, '2010-01-01'),
  ('NV002', NULL, 'PB002', 'Trần Kế B', 'ketoan@example.com', '0900000002', '1987-02-02', 4, '2011-02-01'),
  ('NV003', NULL, 'PB003', 'Lê Định C', 'kiemdinh@example.com', '0900000003', '1989-03-03', 3, '2012-03-01'),
  ('NV004', 'NV001', 'PB001', 'Vũ Thị Kho', 'kho.vt@company.com', '0911234567', '1990-11-15', 3, '2015-03-10'),
('NV005', 'NV001', 'PB001', 'Phạm Văn Hàng', 'hang.pv@company.com', '0917654321', '1992-06-18', 3, '2016-07-22'),

('NV006', 'NV002', 'PB002', 'Ngô Thị Toán', 'toan.nt@company.com', '0921234567', '1991-01-09', 3, '2014-11-01'),
('NV007', 'NV002', 'PB002', 'Đặng Văn Sổ', 'so.dv@company.com', '0929876543', '1993-08-14', 3, '2017-05-05'),

('NV008', 'NV003', 'PB003', 'Bùi Thị Kiểm', 'kiem.bt@company.com', '0931234567', '1989-12-30', 3, '2013-02-18'),
('NV009', 'NV003', 'PB003', 'Tạ Minh Chất', 'chat.tm@company.com', '0936543210', '1990-04-11', 3, '2016-09-12'),
('NV010', 'NV003', 'PB003', 'Dương Thị Test', 'test.dt@company.com', '0938765432', '1994-10-08', 3, '2018-01-03');


INSERT INTO HOPDONG (MAHD, CHIPHITONG, NGAYBATDAU, NGAYKETTHUC, MANHUONGQUYEN, MAGOI)
VALUES
 ('HD001', 50000000, '2023-01-01', '2026-01-01', 'MNQ01', 'GQ01'),
('HD002', 45000000, '2023-02-01', '2026-02-01', 'MNQ02', 'GQ02'),
('HD003', 60000000, '2023-03-01', '2026-03-01', 'MNQ03', 'GQ03'),
('HD004', 55000000, '2023-04-01', '2026-04-01', 'MNQ04', 'GQ04'),
('HD005', 52000000, '2023-05-01', '2026-05-01', 'MNQ05', 'GQ05'),

('HD006', 48000000, '2023-06-01', '2026-06-01', 'MNQ06', 'GQ01'),
('HD007', 47000000, '2023-07-01', '2026-07-01', 'MNQ07', 'GQ02'),
('HD008', 61000000, '2023-08-01', '2026-08-01', 'MNQ08', 'GQ03'),
('HD009', 53000000, '2023-09-01', '2026-09-01', 'MNQ09', 'GQ04'),
('HD010', 49500000, '2023-10-01', '2026-10-01', 'MNQ10', 'GQ05'),

('HD011', 47000000, '2023-11-01', '2026-11-01', 'MNQ11', 'GQ01'),
('HD012', 55000000, '2023-12-01', '2026-12-01', 'MNQ12', 'GQ02'),
('HD013', 58000000, '2024-01-01', '2027-01-01', 'MNQ13', 'GQ03'),
('HD014', 49000000, '2024-02-01', '2027-02-01', 'MNQ14', 'GQ04'),
('HD015', 52000000, '2024-03-01', '2027-03-01', 'MNQ15', 'GQ05'),
('HD016', 55000000, '2024-04-01', '2027-04-01', 'MNQ01', 'GQ01'),
  ('HD017', 50000000, '2024-05-01', '2027-05-01', 'MNQ02', 'GQ02'),
  ('HD018', 60000000, '2024-06-01', '2027-06-01', 'MNQ03', 'GQ03'),
  ('HD019', 53000000, '2024-07-01', '2027-07-01', 'MNQ04', 'GQ04'),
  ('HD020', 49000000, '2024-08-01', '2027-08-01', 'MNQ05', 'GQ05'),
  
  ('HD021', 51000000, '2024-09-01', '2027-09-01', 'MNQ06', 'GQ01'),
  ('HD022', 53000000, '2024-10-01', '2027-10-01', 'MNQ07', 'GQ02'),
  ('HD023', 55000000, '2024-11-01', '2027-11-01', 'MNQ08', 'GQ03'),
  ('HD024', 56000000, '2024-12-01', '2027-12-01', 'MNQ09', 'GQ04'),
  ('HD025', 49000000, '2025-01-01', '2028-01-01', 'MNQ10', 'GQ05'),
  
  ('HD026', 57000000, '2025-02-01', '2028-02-01', 'MNQ11', 'GQ01'),
  ('HD027', 50000000, '2025-03-01', '2028-03-01', 'MNQ12', 'GQ02'),
  ('HD028', 52000000, '2025-04-01', '2028-04-01', 'MNQ13', 'GQ03'),
  ('HD029', 51000000, '2025-05-01', '2028-05-01', 'MNQ14', 'GQ04'),
  ('HD030', 54000000, '2025-06-01', '2028-06-01', 'MNQ15', 'GQ05');

  
INSERT INTO CUAHANGNHUONGQUYEN (MACH, DIACHI, NGAYKHAITRUONG, MASOTHUE, MANHUONGQUYEN, MAHD)
VALUES
  ('CH016', '123 Le Loi, Quan 1, TP.HCM', '2024-04-15', '0312345693', 'MNQ01', 'HD016'),
  ('CH017', '45 Nguyen Hue, Quan 1, TP.HCM', '2024-05-20', '0312345694', 'MNQ02', 'HD017'),
  ('CH018', '67 Tran Hung Dao, Quan 5, TP.HCM', '2024-06-18', '0312345695', 'MNQ03', 'HD018'),
  ('CH019', '89 Vo Van Tan, Quan 3, TP.HCM', '2024-07-10', '0312345696', 'MNQ04', 'HD019'),
  ('CH020', '101 Cach Mang Thang 8, Quan 10, TP.HCM', '2024-08-05', '0312345697', 'MNQ05', 'HD020'),
  
  ('CH021', '202 Nguyen Van Cu, Quan 5, TP.HCM', '2024-09-15', '0312345698', 'MNQ06', 'HD021'),
  ('CH022', '303 Le Quang Dinh, Binh Thanh, TP.HCM', '2024-10-10', '0312345699', 'MNQ07', 'HD022'),
  ('CH023', '404 Cong Hoa, Tan Binh, TP.HCM', '2024-11-15', '0312345700', 'MNQ08', 'HD023'),
  ('CH024', '505 Phan Xich Long, Phu Nhuan, TP.HCM', '2024-12-01', '0312345701', 'MNQ09', 'HD024'),
  ('CH025', '606 Dien Bien Phu, Binh Thanh, TP.HCM', '2025-01-05', '0312345702', 'MNQ10', 'HD025'),
  
  ('CH026', '707 Le Van Sy, Quan 3, TP.HCM', '2025-02-10', '0312345703', 'MNQ11', 'HD026'),
  ('CH027', '808 Hoang Dieu, Quan 4, TP.HCM', '2025-03-01', '0312345704', 'MNQ12', 'HD027'),
  ('CH028', '909 Truong Sa, Phu Nhuan, TP.HCM', '2025-04-05', '0312345705', 'MNQ13', 'HD028'),
  ('CH029', '1001 Pham Van Dong, Thu Duc, TP.HCM', '2025-05-01', '0312345706', 'MNQ14', 'HD029'),
  ('CH030', '1112 Nguyen Van Qua, Go Vap, TP.HCM', '2025-06-10', '0312345707', 'MNQ15', 'HD030');


INSERT INTO CUAHANGNHUONGQUYEN  VALUES 
('CH001', '123 Le Loi, Quan 1, TP.HCM', '2023-01-15', '0312345678', 'MNQ01', 'HD001'),
('CH002', '45 Nguyen Hue, Quan 1, TP.HCM', '2023-02-20', '0312345679', 'MNQ02', 'HD002'),
('CH003', '67 Tran Hung Dao, Quan 5, TP.HCM', '2023-03-18', '0312345680', 'MNQ03', 'HD003'),
('CH004', '89 Vo Van Tan, Quan 3, TP.HCM', '2023-04-10', '0312345681', 'MNQ04', 'HD004'),
('CH005', '101 Cach Mang Thang 8, Quan 10, TP.HCM', '2023-05-05', '0312345682', 'MNQ05', 'HD005'),

('CH006', '202 Nguyen Van Cu, Quan 5, TP.HCM', '2023-06-12', '0312345683', 'MNQ06', 'HD006'),
('CH007', '303 Le Quang Dinh, Binh Thanh, TP.HCM', '2023-07-09', '0312345684', 'MNQ07', 'HD007'),
('CH008', '404 Cong Hoa, Tan Binh, TP.HCM', '2023-08-15', '0312345685', 'MNQ08', 'HD008'),
('CH009', '505 Phan Xich Long, Phu Nhuan, TP.HCM', '2023-09-01', '0312345686', 'MNQ09', 'HD009'),
('CH010', '606 Dien Bien Phu, Binh Thanh, TP.HCM', '2023-10-10', '0312345687', 'MNQ10', 'HD010'),

('CH011', '707 Le Van Sy, Quan 3, TP.HCM', '2023-11-20', '0312345688', 'MNQ11', 'HD011'),
('CH012', '808 Hoang Dieu, Quan 4, TP.HCM', '2023-12-02', '0312345689', 'MNQ12', 'HD012'),
('CH013', '909 Truong Sa, Phu Nhuan, TP.HCM', '2024-01-11', '0312345690', 'MNQ13', 'HD013'),
('CH014', '1001 Pham Van Dong, Thu Duc, TP.HCM', '2024-02-07', '0312345691', 'MNQ14', 'HD014'),
('CH015', '1112 Nguyen Van Qua, Go Vap, TP.HCM', '2024-03-05', '0312345692', 'MNQ15', 'HD015');

INSERT INTO PHIEUNHAP (MAPHIEUNHAP, MANV, NGAYNHAP)
VALUES
  ('PN001', 'NV001', '2023-01-05 09:15:00'),
  ('PN002', 'NV001', '2023-01-12 14:30:00'),
  ('PN003', 'NV001', '2023-02-03 10:00:00'),
  ('PN004', 'NV001', '2023-02-20 16:45:00'),
  ('PN005', 'NV001', '2023-03-08 08:20:00'),
  ('PN006', 'NV004', '2023-03-25 11:10:00'),
  ('PN007', 'NV004', '2023-04-02 15:55:00'),
  ('PN008', 'NV004', '2023-04-18 13:05:00'),
  ('PN009', 'NV004', '2023-05-07 09:40:00'),
  ('PN010', 'NV004', '2023-05-22 17:30:00'),
  ('PN011', 'NV005', '2023-06-01 10:25:00'),
  ('PN012', 'NV005', '2023-06-15 14:00:00'),
  ('PN013', 'NV005', '2023-07-03 08:50:00'),
  ('PN014', 'NV005', '2023-07-19 16:10:00'),
  ('PN015', 'NV005', '2023-08-06 11:35:00'),
  ('PN016', 'NV001', '2023-08-23 09:05:00'),
  ('PN017', 'NV001', '2023-09-10 15:20:00'),
  ('PN018', 'NV001', '2023-09-28 13:45:00'),
  ('PN019', 'NV001', '2023-10-14 10:55:00'),
  ('PN020', 'NV001', '2023-10-30 17:00:00');


INSERT INTO BANGXACTHUC (MaXacThuc, MANV, GhiChuXT, TinhTrangXT, NgayXT)
VALUES
  ('XT001', 'NV003', 'Đã kiểm tra và nhập đủ số lượng hàng theo đơn PN007', TRUE,  '2023-04-03'),
  ('XT002', 'NV003', 'Xử lý khiếu nại khách hàng về hàng bị vỡ, đã hoàn trả 100%',    TRUE,  '2023-05-11'),
  ('XT003', 'NV003', 'Kiểm tra tồn kho, phát hiện chênh lệch 5 sản phẩm, đã điều chỉnh sổ sách', TRUE,  '2023-06-20'),
  ('XT004', 'NV003', 'Đã tiếp nhận đơn hàng gấp, phối hợp với kho vận giao trong 24h',  TRUE,  '2023-07-15'),
  ('XT005', 'NV003', 'Phát hiện hàng lỗi loạt, đã gửi trả NCC và chờ xử lý đổi mới', FALSE, '2023-08-02'),

  ('XT006', 'NV008', 'Kiểm tra số lượng hàng tồn kho, phát hiện thiếu 2 sản phẩm, đã báo cáo', TRUE, '2023-08-10'),
  ('XT007', 'NV008', 'Tiến hành xử lý đơn hàng gấp, giao hàng trong vòng 12h', TRUE, '2023-08-15'),
  ('XT008', 'NV009', 'Kiểm tra tình trạng hàng hóa trước khi giao cho khách, phát hiện sản phẩm bị lỗi', FALSE, '2023-08-20'),
  ('XT009', 'NV009', 'Đã tiếp nhận đơn hàng và xử lý theo yêu cầu của khách hàng, giao đúng hẹn', TRUE, '2023-09-01'),
  ('XT010', 'NV010', 'Kiểm tra và xác nhận tồn kho, phát hiện sai sót trong sổ sách, đã chỉnh sửa', TRUE, '2023-09-05'),
  ('XT011', 'NV010', 'Kiểm tra đơn hàng chưa giao và liên hệ khách hàng để phối hợp giao hàng', TRUE, '2023-09-10'),
  ('XT012', 'NV008', 'Phát hiện hàng lỗi loạt, đã gửi trả NCC và yêu cầu đổi mới', FALSE, '2023-09-15'),
  ('XT013', 'NV009', 'Đã hoàn thành kiểm tra tồn kho và điều chỉnh lại số lượng sản phẩm', TRUE, '2023-09-18'),
  ('XT014', 'NV008', 'Kiểm tra tình trạng hàng hóa trước khi xuất kho, đảm bảo chất lượng sản phẩm', TRUE, '2023-09-25'),
  ('XT015', 'NV010', 'Đã xử lý đơn hàng khẩn cấp và giao hàng đúng hạn, báo cáo kết quả', TRUE, '2023-09-30');

INSERT INTO BANGCAP (
  SOHIEUBANG, SOVAOSO, MANV,
  NGAYCAPBANG, XEPLOAI, HINHTHUCDAOTAO,
  NGUOICAP, CHUYENNGANHDAOTAO,
  THOIGIANDAOTAO, THOIGIANKETTHUCDAOTAO, NOICAP
)
VALUES
  ('BC001', 'VS1234567890', 'NV001',
   '2015-06-20', 'Giỏi',      'Chính quy',
   'Đại học Quốc gia TP.HCM', 'Quản trị kinh doanh',
   '2011-09-01', '2015-06-15', 'TP.HCM'),

  ('BC002', 'VS0987654321', 'NV002',
   '2017-11-10', 'Khá',       'Liên thông',
   'Đại học Kinh tế Quốc dân', 'Kế toán',
   '2013-09-01', '2017-10-30', 'Hà Nội'),

  ('BC003', 'VS1122334455', 'NV003',
   '2019-05-25', 'Xuất sắc',  'Vừa làm vừa học',
   'Học viện Ngân hàng',     'Quản lý chất lượng',
   '2015-09-01', '2019-05-20', 'Hà Nội'),

  ('BC004', 'VS1234578901', 'NV004',
   '2016-05-18', 'Giỏi', 'Chính quy',
   'Đại học Bách Khoa TP.HCM', 'Kỹ thuật cơ khí',
   '2011-09-01', '2016-05-15', 'TP.HCM'),

  ('BC005', 'VS2234567890', 'NV005',
   '2018-09-12', 'Khá', 'Liên thông',
   'Đại học Mở TP.HCM', 'Marketing',
   '2014-09-01', '2018-09-10', 'TP.HCM'),

  ('BC006', 'VS3345678901', 'NV006',
   '2020-08-15', 'Xuất sắc', 'Vừa làm vừa học',
   'Đại học Kinh tế TP.HCM', 'Tài chính - Ngân hàng',
   '2016-09-01', '2020-08-10', 'TP.HCM'),

  ('BC007', 'VS4456789012', 'NV007',
   '2021-03-22', 'Giỏi', 'Chính quy',
   'Đại học Ngoại thương', 'Kinh tế đối ngoại',
   '2015-09-01', '2021-03-15', 'Hà Nội'),

  ('BC008', 'VS5567890123', 'NV008',
   '2022-01-20', 'Khá', 'Liên thông',
   'Đại học Sư phạm TP.HCM', 'Giáo dục Tiểu học',
   '2018-09-01', '2022-01-18', 'TP.HCM'),

  ('BC009', 'VS6678901234', 'NV009',
   '2023-02-18', 'Xuất sắc', 'Vừa làm vừa học',
   'Đại học Công nghiệp TP.HCM', 'Kỹ thuật điện tử',
   '2017-09-01', '2023-02-15', 'TP.HCM'),

  ('BC010', 'VS7789012345', 'NV010',
   '2021-11-05', 'Giỏi', 'Chính quy',
   'Đại học Kinh tế Quốc dân', 'Kinh tế học',
   '2014-09-01', '2021-11-03', 'Hà Nội');

INSERT INTO NGUOITHAN (IDNT,TENNT, QUANHE, MANV, SDTNT)
VALUES
  -- Người thân của NV001
  (1,'Nguyễn Văn Hòa',     'Cha',      'NV001', '0912340001'),
  (2,'Trần Thị Lan',       'Mẹ',       'NV001', '0912340002'),

  -- Người thân của NV002
  (3,'Lê Thị Hồng',        'Vợ',       'NV002', '0909871001'),
  (4,'Phạm Văn Hùng',      'Con trai', 'NV002', '0909871002'),

  -- Người thân của NV003
  (5,'Hoàng Văn Long',     'Anh trai', 'NV003', '0901234001'),
  (6,'Bùi Thị Hoa',        'Mẹ',       'NV003', '0901234002'),

  -- Người thân của NV004
  (7,'Nguyễn Văn Tâm',     'Cha',      'NV004', '0912345670'),
  (8,'Trần Thị Như',       'Chị gái',  'NV004', '0912345671'),

  -- Người thân của NV005
  (9,'Lê Văn Hòa',         'Chồng',    'NV005', '0912345672'),
  (10,'Phạm Thị Hà',        'Con gái',  'NV005', '0912345673'),

  -- Người thân của NV006
  (11,'Hoàng Thị Mai',      'Mẹ',       'NV006', '0912345674'),
  (12,'Bùi Văn Quang',      'Em trai',  'NV006', '0912345675'),

  -- Người thân của NV007
  (13,'Nguyễn Thị Hạnh',    'Vợ',       'NV007', '0912345676'),
  (14,'Trần Văn Thắng',     'Cha',      'NV007', '0912345677'),

  -- Người thân của NV008
  (15,'Lê Văn Bình',        'Anh rể',   'NV008', '0912345678'),
  (16,'Phạm Thị Thảo',      'Chị gái',  'NV008', '0912345679'),

  -- Người thân của NV009
  (17,'Hoàng Văn Cường',    'Cha',      'NV009', '0912345680'),
  (18,'Bùi Thị Loan',       'Mẹ',       'NV009', '0912345681'),

  -- Người thân của NV010
  (19,'Nguyễn Thị Tươi',    'Vợ',       'NV010', '0912345682'),
  (20,'Trần Văn Minh',      'Con trai', 'NV010', '0912345683');


  INSERT INTO LyLich (
  TrinhDoVanHoa,
  DanToc,
  TonGiao,
  TrinhDoChuyenMon,
  NoiThuongTru,
  NoiTamTru,
  NoiSinh,
  MANV
)
VALUES
  (
    '12/12',         -- Trình độ văn hóa
    'Kinh',          -- Dân tộc
    'Không',         -- Tôn giáo
    'Cử nhân QTKD',  -- Trình độ chuyên môn
    '123 Lê Lợi, TP.HCM',  -- Nơi thường trú
    '456 Trần Phú, Q.5, TP.HCM', -- Nơi tạm trú
    'Hà Nội',        -- Nơi sinh
    'NV001'
  ),
  (
    '12/12',
    'Tày',
    'Phật giáo',
    'Cử nhân Kế toán',
    '78 Nguyễn Trãi, Hà Nội',
    '90 Trần Duy Hưng, Hà Nội',
    'Hà Nội',
    'NV002'
  ),
  (
    '12/12',
    'Hoa',
    'Không',
    'Cử nhân Quản lý chất lượng',
    '15 Nguyễn Văn Cừ, Đà Nẵng',
    '20 Bạch Đằng, Đà Nẵng',
    'Đà Nẵng',
    'NV003'
  ),

 -- LyLich của NV004
  (
    '12/12',         -- Trình độ văn hóa
    'Kinh',          -- Dân tộc
    'Không',         -- Tôn giáo
    'Cử nhân Kỹ thuật',  -- Trình độ chuyên môn
    '123 Lê Lợi, TP.HCM',  -- Nơi thường trú
    '456 Trần Phú, Q.5, TP.HCM', -- Nơi tạm trú
    'Hà Nội',        -- Nơi sinh
    'NV004'
  ),
  -- LyLich của NV005
  (
    '12/12',
    'Tày',
    'Phật giáo',
    'Cử nhân Kế toán',
    '78 Nguyễn Trãi, Hà Nội',
    '90 Trần Duy Hưng, Hà Nội',
    'Hà Nội',
    'NV005'
  ),
  -- LyLich của NV006
  (
    '12/12',
    'Hoa',
    'Không',
    'Cử nhân Quản lý chất lượng',
    '15 Nguyễn Văn Cừ, Đà Nẵng',
    '20 Bạch Đằng, Đà Nẵng',
    'Đà Nẵng',
    'NV006'
  ),
  -- LyLich của NV007
  (
    '12/12',
    'Tày',
    'Phật giáo',
    'Cử nhân Công nghệ thông tin',
    '22 Lê Quang Định, TP.HCM',
    '45 Trần Hưng Đạo, TP.HCM',
    'TP.HCM',
    'NV007'
  ),
  -- LyLich của NV008
  (
    '12/12',
    'Kinh',
    'Không',
    'Cử nhân Quản trị kinh doanh',
    '44 Đường Láng, Hà Nội',
    '77 Hồ Tùng Mậu, Hà Nội',
    'Hà Nội',
    'NV008'
  ),
  -- LyLich của NV009
  (
    '12/12',
    'H mông',
    'Công giáo',
    'Thạc sĩ Quản lý kinh tế',
    '66 Phan Đình Phùng, TP.HCM',
    '89 Nguyễn Văn Linh, TP.HCM',
    'Hà Nội',
    'NV009'
  ),
  -- LyLich của NV010
  (
    '12/12',
    'Kinh',
    'Không',
    'Thạc sĩ Kỹ thuật phần mềm',
    '88 Trần Thái Tông, TP.HCM',
    '121 Bùi Hữu Nghĩa, TP.HCM',
    'Hà Nội',
    'NV010'
  );

INSERT INTO HANG (MAHANG, MAKHO, TENHANG, DONVIDOLUONG, GIANHAP, GIABAN, LOAIHANG)
VALUES
('H001', 'K01', 'Sữa tươi Vinamilk', 'Lít', 12000, 15000, 'Đồ uống'),
('H002', 'K01', 'Nước ngọt Coca-Cola', 'Chai', 8000, 10000, 'Đồ uống'),
('H003', 'K02', 'Nước ép trái cây 100%', 'Chai', 15000, 18000, 'Đồ uống'),
('H004', 'K02', 'Cafe hòa tan Nestlé', 'Gói', 35000, 45000, 'Đồ uống'),
('H005', 'K03', 'Bánh mì thịt', 'Cái', 10000, 15000, 'Thực phẩm chế biến sẵn'),
('H006', 'K03', 'Bánh bao chay', 'Cái', 5000, 7000, 'Thực phẩm chế biến sẵn'),
('H007', 'K04', 'Mì ăn liền Vina', 'Gói', 3000, 4000, 'Thực phẩm chế biến sẵn'),
('H008', 'K04', 'Gà rán KFC', 'Phần', 30000, 35000, 'Thực phẩm chế biến sẵn'),
('H009', 'K05', 'Cơm hộp', 'Hộp', 15000, 18000, 'Thực phẩm chế biến sẵn'),
('H010', 'K05', 'Xôi gà', 'Cái', 12000, 15000, 'Thực phẩm chế biến sẵn'),
('H011', 'K01', 'Trái cây tươi', 'Kg', 50000, 60000, 'Trái cây'),
('H012', 'K01', 'Chuối', 'Kg', 20000, 25000, 'Trái cây'),
('H013', 'K02', 'Dưa hấu', 'Kg', 15000, 20000, 'Trái cây'),
('H014', 'K02', 'Cam', 'Kg', 25000, 30000, 'Trái cây'),
('H015', 'K03', 'Táo', 'Kg', 30000, 35000, 'Trái cây'),
('H016', 'K03', 'Nho', 'Kg', 45000, 50000, 'Trái cây'),
('H017', 'K04', 'Mít', 'Kg', 20000, 25000, 'Trái cây'),
('H018', 'K04', 'Lê', 'Kg', 35000, 40000, 'Trái cây'),
('H019', 'K05', 'Quýt', 'Kg', 15000, 20000, 'Trái cây'),
('H020', 'K05', 'Ổi', 'Kg', 20000, 25000, 'Trái cây'),
('H021', 'K01', 'Bánh tráng cuốn', 'Cái', 3000, 5000, 'Món ăn vặt'),
('H022', 'K01', 'Kẹo dẻo', 'Gói', 4000, 6000, 'Món ăn vặt'),
('H023', 'K02', 'Snack khoai tây', 'Gói', 5000, 7000, 'Món ăn vặt'),
('H024', 'K02', 'Bánh quy', 'Gói', 6000, 8000, 'Món ăn vặt'),
('H025', 'K03', 'Kem', 'Cây', 7000, 9000, 'Món ăn vặt'),
('H026', 'K03', 'Nước đá', 'Cây', 2000, 4000, 'Món ăn vặt'),
('H027', 'K04', 'Chân gà nướng', 'Cái', 8000, 10000, 'Món ăn vặt'),
('H028', 'K04', 'Bánh mì kẹp thịt', 'Cái', 15000, 20000, 'Món ăn vặt'),
('H029', 'K05', 'Soda', 'Chai', 10000, 15000, 'Đồ uống'),
('H030', 'K05', 'Bia', 'Chai', 20000, 30000, 'Đồ uống'),
('H031', 'K01', 'Nước suối', 'Chai', 4000, 6000, 'Đồ uống'),
('H032', 'K01', 'Trà sữa', 'Ly', 15000, 20000, 'Đồ uống'),
('H033', 'K02', 'Cà phê đen', 'Ly', 12000, 15000, 'Đồ uống'),
('H034', 'K02', 'Cà phê sữa', 'Ly', 15000, 20000, 'Đồ uống'),
('H035', 'K03', 'Trà đào', 'Ly', 18000, 22000, 'Đồ uống'),
('H036', 'K03', 'Nước ép cà chua', 'Ly', 16000, 18000, 'Đồ uống'),
('H037', 'K04', 'Cà phê đá', 'Ly', 17000, 20000, 'Đồ uống'),
('H038', 'K04', 'Trà chanh', 'Ly', 13000, 16000, 'Đồ uống'),
('H039', 'K05', 'Nước yến', 'Chai', 25000, 30000, 'Đồ uống'),
('H040', 'K05', 'Sữa đậu nành', 'Chai', 8000, 10000, 'Đồ uống'),
('H041', 'K01', 'Mì tôm', 'Gói', 3000, 5000, 'Thực phẩm chế biến sẵn'),
('H042', 'K01', 'Cơm sườn', 'Hộp', 20000, 25000, 'Thực phẩm chế biến sẵn'),
('H043', 'K02', 'Phở', 'Hộp', 25000, 30000, 'Thực phẩm chế biến sẵn'),
('H044', 'K02', 'Bánh xèo', 'Cái', 10000, 15000, 'Thực phẩm chế biến sẵn'),
('H045', 'K03', 'Cháo gà', 'Hộp', 15000, 20000, 'Thực phẩm chế biến sẵn'),
('H046', 'K03', 'Mì xào', 'Gói', 12000, 15000, 'Thực phẩm chế biến sẵn'),
('H047', 'K04', 'Bánh bao', 'Cái', 6000, 8000, 'Thực phẩm chế biến sẵn'),
('H048', 'K04', 'Sushi', 'Cái', 20000, 25000, 'Thực phẩm chế biến sẵn'),
('H049', 'K05', 'Bánh mì chảo', 'Cái', 12000, 15000, 'Thực phẩm chế biến sẵn'),
('H050', 'K05', 'Cơm tấm', 'Hộp', 20000, 25000, 'Thực phẩm chế biến sẵn');

INSERT INTO PHIEUXUAT (MAPHIEUXUAT, MACH, NGAYXUAT, THOIGIANNHAPLIEU, TINHTRANGNHAPLIEU)
VALUES
  ('PX001',  'CH001', '2024-12-01 09:00:00', '2024-12-01 12:00:00', 1),
  ('PX002',  'CH002', '2024-12-02 10:00:00', '2024-12-02 13:15:00', 1),
  ('PX003',  'CH003', '2024-12-03 08:30:00', '2024-12-03 11:30:00', 1),
  ('PX004',  'CH004', '2024-12-04 09:15:00', '2024-12-04 12:30:00', 1),
  ('PX005',  'CH005', '2024-12-05 10:45:00', '2024-12-05 14:00:00', 1),

  ('PX006',  'CH006', '2024-12-06 11:00:00', '2024-12-06 15:10:00', 1),
  ('PX007',  'CH007', '2024-12-07 09:30:00', '2024-12-07 12:30:00', 1),
  ('PX008',  'CH008', '2024-12-08 08:15:00', '2024-12-08 11:45:00', 1),
  ('PX009',  'CH009', '2024-12-09 10:00:00', '2024-12-09 13:00:00', 1),
  ('PX010',  'CH010', '2024-12-10 09:00:00', '2024-12-10 12:00:00', 1),

  ('PX011',  'CH011', '2024-12-11 09:30:00', '2024-12-11 13:30:00', 1),
  ('PX012',  'CH012', '2024-12-12 10:00:00', '2024-12-12 14:00:00', 1),
  ('PX013',  'CH013', '2024-12-13 08:45:00', '2024-12-13 11:45:00', 1),
  ('PX014',  'CH014', '2024-12-14 09:20:00', '2024-12-14 12:20:00', 1),
  ('PX015',  'CH015', '2024-12-15 10:10:00', '2024-12-15 13:40:00', 1),

  ('PX016',  'CH016', '2024-12-16 09:00:00', '2024-12-16 12:30:00', 1),
  ('PX017',  'CH017', '2024-12-17 10:30:00', '2024-12-17 13:50:00', 1),
  ('PX018',  'CH018', '2024-12-18 08:50:00', '2024-12-18 11:50:00', 1),
  ('PX019',  'CH019', '2024-12-19 09:40:00', '2024-12-19 13:00:00', 1),
  ('PX020',  'CH020', '2024-12-20 10:20:00', '2024-12-20 14:00:00', 1);

INSERT INTO CTPN (MAPHIEUNHAP, MAHANG, SOLUONGNHAP, DONGIANHAP)
VALUES
('PN001', 'H001',  50,  15000),
('PN002', 'H005',  30,  22000),
('PN003', 'H010',  40,  18000),
('PN004', 'H003',  60,  20000),
('PN005', 'H015',  25,  25000),

('PN006', 'H008',  35,  19500),
('PN007', 'H012',  45,  21000),
('PN008', 'H020',  50,  17500),
('PN009', 'H018',  20,  24000),
('PN010', 'H025',  30,  23000),

('PN011', 'H007',  40,  16000),
('PN012', 'H014',  55,  20000),
('PN013', 'H022',  28,  19000),
('PN014', 'H030',  38,  18500),
('PN015', 'H033',  33,  17000),

('PN016', 'H017',  60,  26000),
('PN017', 'H041',  22,  19500),
('PN018', 'H045',  25,  22500),
('PN019', 'H036',  45,  20000),
('PN020', 'H050',  30,  21000);

INSERT INTO CTPX (MAPHIEUXUAT, MAHANG, SOLUONGXUAT, DONGIAXUAT, DONVITINH, GIAMGIABAN)
VALUES
('PX001', 'H001',  20,  20000, 'Hộp', NULL),
('PX002', 'H005',  15,  25000, 'Thùng', 5000),
('PX003', 'H010',  25,  23000, 'Cái', NULL),
('PX004', 'H003',  30,  22000, 'Kg', 1000),
('PX005', 'H015',  10,  27000, 'Lốc', NULL),

('PX006', 'H008',  18,  21000, 'Hộp', 8000),
('PX007', 'H012',  22,  24000, 'Thùng', NULL),
('PX008', 'H020',  20,  20000, 'Kg', NULL),
('PX009', 'H018',  12,  26000, 'Hộp', 5000),
('PX010', 'H025',  15,  25000, 'Cái', NULL),

('PX011', 'H007',  25,  19000, 'Lốc', NULL),
('PX012', 'H014',  28,  21000, 'Hộp', 7000),
('PX013', 'H022',  20,  21500, 'Kg', NULL),
('PX014', 'H030',  30,  19500, 'Cái', NULL),
('PX015', 'H033',  18,  18500, 'Thùng', 4000),

('PX016', 'H017',  35,  27000, 'Lít', NULL),
('PX017', 'H041',  16,  23000, 'Cái', 6000),
('PX018', 'H045',  20,  24500, 'Thùng', NULL),
('PX019', 'H036',  25,  21500, 'Kg', NULL),
('PX020', 'H050',  20,  22500, 'Hộp', 5000);


INSERT INTO BAOCAO (MABAOCAO, MaXacThuc, MACH, LOAIBAOCAO, NGAYBAOCAO, NOIDUNGBAOCAO)
VALUES
  -- Các báo cáo cho XT001
  ('BC001', 'XT001', 'CH001', 'Khiếu nại', '2024-01-10 10:15:00', 'Khách hàng phản ánh hàng bị hư hỏng khi nhận. Đã xử lý đổi trả.'),
  ('BC002', 'XT001', 'CH002', 'Chất lượng', '2024-01-12 09:45:00', 'Kiểm định chất lượng sản phẩm lô hàng MH005. Đạt tiêu chuẩn.'),
  
  -- Các báo cáo cho XT002
  ('BC003', 'XT002', 'CH003', 'Nhập kho', '2024-01-15 14:00:00', 'Cửa hàng đã hoàn tất nhập lô hàng MH010 theo phiếu PN003.'),
  ('BC004', 'XT002', 'CH004', 'Xuất kho', '2024-01-20 11:30:00', 'Đã xuất 30 đơn vị MH003 cho khách hàng. Không có sai sót.'),
  
  -- Các báo cáo cho XT003
  ('BC005', 'XT003', 'CH005', 'Tồn kho', '2024-01-25 16:10:00', 'Kiểm kê tồn kho quý I. Số lượng khớp dữ liệu.'),
  ('BC006', 'XT003', 'CH006', 'Khiếu nại', '2024-01-27 13:20:00', 'Khách phản ánh giao thiếu sản phẩm. Đã hoàn tất bổ sung.'),
  
  -- Các báo cáo cho XT004
  ('BC007', 'XT004', 'CH007', 'Bảo trì', '2024-01-30 08:50:00', 'Kiểm tra máy lạnh tại cửa hàng. Đã sửa chữa xong.'),
  ('BC008', 'XT004', 'CH008', 'Chất lượng', '2024-02-02 09:00:00', 'Phát hiện bao bì rách lô hàng MH014. Đã tách kho.'),
  
  -- Các báo cáo cho XT005
  ('BC009', 'XT005', 'CH009', 'Kiểm kê', '2024-02-05 15:30:00', 'Đồng bộ số liệu kho MH018. Phát hiện thiếu 5 đơn vị.'),
  ('BC010', 'XT005', 'CH010', 'Khác', '2024-02-10 10:00:00', 'Báo cáo nội bộ: lắp đặt camera an ninh mới.'),

  -- Các báo cáo cho XT006
  ('BC011', 'XT006', 'CH011', 'Tồn kho', '2024-02-12 14:30:00', 'Kiểm tra tồn kho cho lô hàng MH020. Đã xác nhận đủ số lượng.'),
  ('BC012', 'XT006', 'CH012', 'Nhập kho', '2024-02-15 11:00:00', 'Cập nhật thông tin kho theo phiếu nhập kho PN021.'),
  
  -- Các báo cáo cho XT007
  ('BC013', 'XT007', 'CH013', 'Xuất kho', '2024-02-18 09:00:00', 'Đã hoàn tất xuất kho 40 đơn vị MH022.'),
  ('BC014', 'XT007', 'CH014', 'Chất lượng', '2024-02-20 10:30:00', 'Kiểm định chất lượng sản phẩm lô hàng MH023. Đạt yêu cầu.'),
  
  -- Các báo cáo cho XT008
  ('BC015', 'XT008', 'CH015', 'Khiếu nại', '2024-02-22 13:00:00', 'Khách hàng phản ánh sản phẩm bị lỗi khi nhận. Đã xử lý đổi trả.'),
  ('BC016', 'XT008', 'CH016', 'Bảo trì', '2024-02-25 16:00:00', 'Kiểm tra máy lạnh tại cửa hàng MH024, đã sửa chữa xong.'),

  -- Các báo cáo cho XT009
  ('BC017', 'XT009', 'CH017', 'Kiểm kê', '2024-02-28 11:15:00', 'Đồng bộ số liệu kho cho lô MH025. Phát hiện thiếu 3 đơn vị.'),
  ('BC018', 'XT009', 'CH018', 'Khác', '2024-03-02 09:00:00', 'Báo cáo tình trạng hàng hóa trong kho sau khi kiểm kê.'),

  -- Các báo cáo cho XT010
  ('BC019', 'XT010', 'CH019', 'Chất lượng', '2024-03-05 14:00:00', 'Kiểm tra chất lượng hàng hóa, phát hiện sản phẩm lỗi, đã gửi về NCC.'),
  ('BC020', 'XT010', 'CH020', 'Khiếu nại', '2024-03-08 13:30:00', 'Khách hàng khiếu nại hàng bị vỡ trong quá trình vận chuyển. Đã xử lý hoàn tiền.'),

  -- Các báo cáo cho XT011
  ('BC021', 'XT011', 'CH021', 'Nhập kho', '2024-03-10 08:45:00', 'Cập nhật tình trạng kho, đã nhập đủ số lượng hàng hóa.'),
  ('BC022', 'XT011', 'CH022', 'Tồn kho', '2024-03-12 10:00:00', 'Kiểm tra tình trạng hàng hóa tồn kho, không có sai sót.'),

  -- Các báo cáo cho XT012
  ('BC023', 'XT012', 'CH023', 'Bảo trì', '2024-03-15 14:30:00', 'Kiểm tra hệ thống điện tại cửa hàng, đã hoàn tất bảo trì.'),
  ('BC024', 'XT012', 'CH024', 'Xuất kho', '2024-03-18 09:30:00', 'Xuất kho hàng hóa theo đơn yêu cầu. Không có sai sót.'),

  -- Các báo cáo cho XT013
  ('BC025', 'XT013', 'CH025', 'Khác', '2024-03-20 10:00:00', 'Báo cáo tình hình tồn kho sau khi kiểm tra. Đã điều chỉnh số lượng đúng.'),

  -- Các báo cáo cho XT014
  ('BC026', 'XT014', 'CH026', 'Khiếu nại', '2024-03-22 13:30:00', 'Khách hàng phản ánh thiếu sản phẩm trong đơn hàng, đã bổ sung giao hàng mới.'),
  
  -- Các báo cáo cho XT015
  ('BC027', 'XT015', 'CH027', 'Chất lượng', '2024-03-25 11:45:00', 'Kiểm định chất lượng sản phẩm lô MH028. Đạt tiêu chuẩn.'),
  ('BC028', 'XT015', 'CH028', 'Nhập kho', '2024-03-28 09:15:00', 'Hoàn thành nhập kho theo phiếu PN029. Đủ số lượng sản phẩm.');
INSERT INTO BAOCAO (MABAOCAO, MaXacThuc, MACH, LOAIBAOCAO, NGAYBAOCAO, NOIDUNGBAOCAO, DOANHTHU)
VALUES
    ('BC029', 'XT001', 'CH001', 'Doanh Thu', '2024-01-05 09:00:00', 'Báo cáo doanh thu tháng 1 - CH001', 20000000),
    ('BC030', 'XT002', 'CH002', 'Doanh Thu', '2024-01-18 14:15:00', 'Báo cáo doanh thu tháng 1 - CH002', 21500000),
    
    ('BC031', 'XT003', 'CH003', 'Doanh Thu', '2024-02-03 10:00:00', 'Báo cáo doanh thu tháng 2 - CH003', 18000000),
    ('BC032', 'XT004', 'CH004', 'Doanh Thu', '2024-02-21 16:45:00', 'Báo cáo doanh thu tháng 2 - CH004', 22000000),
    ('BC033', 'XT005', 'CH005', 'Doanh Thu', '2024-02-28 08:30:00', 'Báo cáo doanh thu tháng 2 - CH005', 19500000),

    ('BC034', 'XT006', 'CH006', 'Doanh Thu', '2024-03-06 11:00:00', 'Báo cáo doanh thu tháng 3 - CH006', 25000000),
    ('BC035', 'XT007', 'CH007', 'Doanh Thu', '2024-03-19 09:20:00', 'Báo cáo doanh thu tháng 3 - CH007', 21000000),
    ('BC036', 'XT008', 'CH008', 'Doanh Thu', '2024-03-27 13:50:00', 'Báo cáo doanh thu tháng 3 - CH008', 23000000),

    ('BC037', 'XT009', 'CH009', 'Doanh Thu', '2024-04-02 10:30:00', 'Báo cáo doanh thu tháng 4 - CH009', 27500000),
    ('BC038', 'XT010', 'CH010', 'Doanh Thu', '2024-04-15 09:10:00', 'Báo cáo doanh thu tháng 4 - CH010', 19000000),
    ('BC039', 'XT011', 'CH011', 'Doanh Thu', '2024-04-28 18:40:00', 'Báo cáo doanh thu tháng 4 - CH011', 26000000),

    ('BC040', 'XT012', 'CH012', 'Doanh Thu', '2024-05-03 09:25:00', 'Báo cáo doanh thu tháng 5 - CH012', 21500000),
    ('BC041', 'XT013', 'CH013', 'Doanh Thu', '2024-05-17 12:15:00', 'Báo cáo doanh thu tháng 5 - CH013', 18500000),
    ('BC042', 'XT014', 'CH014', 'Doanh Thu', '2024-05-26 15:00:00', 'Báo cáo doanh thu tháng 5 - CH014', 27000000),

    ('BC043', 'XT015', 'CH015', 'Doanh Thu', '2024-06-05 10:20:00', 'Báo cáo doanh thu tháng 6 - CH015', 22500000),
    ('BC044', 'XT001', 'CH016', 'Doanh Thu', '2024-06-19 09:40:00', 'Báo cáo doanh thu tháng 6 - CH016', 24500000),

    ('BC045', 'XT002', 'CH017', 'Doanh Thu', '2024-07-01 09:10:00', 'Báo cáo doanh thu tháng 7 - CH017', 20000000),
    ('BC046', 'XT003', 'CH018', 'Doanh Thu', '2024-07-22 08:50:00', 'Báo cáo doanh thu tháng 7 - CH018', 21500000),

    ('BC047', 'XT004', 'CH019', 'Doanh Thu', '2024-08-07 09:30:00', 'Báo cáo doanh thu tháng 8 - CH019', 18000000),
    ('BC048', 'XT005', 'CH020', 'Doanh Thu', '2024-08-24 10:15:00', 'Báo cáo doanh thu tháng 8 - CH020', 21000000),

    ('BC049', 'XT006', 'CH021', 'Doanh Thu', '2024-09-12 09:45:00', 'Báo cáo doanh thu tháng 9 - CH021', 26500000),
    ('BC050', 'XT007', 'CH022', 'Doanh Thu', '2024-09-28 17:30:00', 'Báo cáo doanh thu tháng 9 - CH022', 20500000),

    ('BC051', 'XT008', 'CH023', 'Doanh Thu', '2024-10-04 09:20:00', 'Báo cáo doanh thu tháng 10 - CH023', 23500000),
    ('BC052', 'XT009', 'CH024', 'Doanh Thu', '2024-10-21 09:35:00', 'Báo cáo doanh thu tháng 10 - CH024', 19000000),

    ('BC053', 'XT010', 'CH025', 'Doanh Thu', '2024-11-05 10:00:00', 'Báo cáo doanh thu tháng 11 - CH025', 25500000),
    ('BC054', 'XT011', 'CH026', 'Doanh Thu', '2024-11-18 09:50:00', 'Báo cáo doanh thu tháng 11 - CH026', 23000000),

    ('BC055', 'XT012', 'CH027', 'Doanh Thu', '2024-12-03 09:30:00', 'Báo cáo doanh thu tháng 12 - CH027', 17500000),
    ('BC056', 'XT013', 'CH028', 'Doanh Thu', '2024-12-16 10:10:00', 'Báo cáo doanh thu tháng 12 - CH028', 28000000),
    ('BC057', 'XT014', 'CH029', 'Doanh Thu', '2024-12-24 08:55:00', 'Báo cáo doanh thu tháng 12 - CH029', 19000000),
    ('BC058', 'XT015', 'CH030', 'Doanh Thu', '2024-12-30 09:15:00', 'Báo cáo doanh thu tháng 12 - CH030', 22500000);


select*From goinhuongquyen

