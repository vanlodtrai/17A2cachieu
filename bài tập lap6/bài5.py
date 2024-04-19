day_so=input("Nhập dãy số nguyên,cách nhau bằng dấu cách: ").split()

ds_nguyen=[int(so) for so in day_so]
la_cap_so_cong=True
if len(ds_nguyen)<3:
    la_cap_so_cong=False
else:
    for i in range(2,len(ds_nguyen)):
        if ds_nguyen[i]-ds_nguyen[i - 1]!=ds_nguyen[1]-ds_nguyen[0]:
            la_cap_so_cong=False
            break
if la_cap_so_cong:
    print("Dãy số tạo thành cấp số cộng:",ds_nguyen)
else:
    print("Dãy số không tạo thành cấp số cộng.")