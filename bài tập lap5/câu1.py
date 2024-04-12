so_nhi_phan=""
n=int(input("Nhập số nguyên dương: "))
if n<0:
    print("Nhập số nguyên dương")
else:
    while n>0:
        phan_du=n%2
        so_nhi_phan=str(phan_du)+so_nhi_phan
        n=n//2
    print("Số nhị phân sau khi chuyển đổi là: ",so_nhi_phan)