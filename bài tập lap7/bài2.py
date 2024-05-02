d_sach={}
for i in range(10):
    ten = input("Nhập tên sinh viên"+str(i+1)+":")
    diem_thi = int(input("Nhap diem thi: "))
    d_sach[ten] = diem_thi

danh_sach_xep_loai = {'F': 0, 'D': 0, 'C': 0, 'B': 0, 'A': 0}
for ten, diem_thi in d_sach.items():
    if diem_thi >= 8.5:
        danh_sach_xep_loai['A'] += 1
    elif diem_thi >= 7.0 and diem_thi < 8.5:
        danh_sach_xep_loai['B'] += 1
    elif diem_thi >= 5.5 and diem_thi < 7.0:
        danh_sach_xep_loai['C'] += 1
    elif diem_thi >= 4.0 and diem_thi < 5.5:
        danh_sach_xep_loai['D'] += 1
    else:
        danh_sach_xep_loai['F'] += 1
        
print("Thống kê số lượng sinh viên ở mỗi loại học lực: ")
print(danh_sach_xep_loai)