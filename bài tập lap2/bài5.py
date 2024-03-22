so_nguoi = int(input("Nhập số lượng người: "))
gia_ve = 120000

if so_nguoi>=2 and so_nguoi<=4:
    so_tien = (gia_ve-(gia_ve * 0.05))*so_nguoi
    print("Số tiền phải trả: ",so_tien)
elif so_nguoi>4 and so_nguoi<=10:
    so_tien = (gia_ve-(gia_ve * 0.05))*so_nguoi
    print("Số tiền phải trả: ",so_tien)
elif so_nguoi>10:
    so_tien = (gia_ve-(gia_ve * 0.05))*so_nguoi
    print("Số tiền phải trả: ",so_tien)
else:
    so_tien = gia_ve * so_nguoi    
    print("Số tiền phải trả: ",so_tien)