n = int(input("Nhập số Fibonacci bạn muốn tạo: "))
ds_fibonacci=[0,1] if n>1 else [0] if n==1 else []

if n>2:
    for i in range(2, n):
        ds_fibonacci.append(ds_fibonacci[-1] + ds_fibonacci[-2])

print("Dãy Fibonacci:",ds_fibonacci)

ds_so_nguyen_to = [so for so in range(2, 100) if all(so%i!= 0 for i in range(2,int(so**0.5)+1))]

print("Danh sách số nguyên tố nhỏ hơn 100:",ds_so_nguyen_to)