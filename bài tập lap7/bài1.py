nguyen_huu_van = {}
n=int(input("Nhập n: "))
for x in range(1,n+1):
    nguyen_huu_van[x]=x**3
print(f"từ điển là các phần tử mà có key là x và value của key là x3 có độ dài {n} là: \n", nguyen_huu_van)