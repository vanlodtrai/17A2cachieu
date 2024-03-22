
a=int(input("Nhập số nguyên thứ nhất: "))
b=int(input("Nhập số nguyên thứ hai: "))
c=int(input("Nhập số nguyên thứ ba: "))
if a>=b>=c or c>=b>=a:
    so_lon_thu_2 = b
elif b>=a>=c or c>=a>= b:
    so_lon_thu_2 =a
else:
    so_lon_thu_2 =c

print("Số lớn thứ hai trong ba số là:",so_lon_thu_2)
