chuỗi=input("Nhập một chuỗi để kiểm tra: ").split()
count=0
chuỗi_đặc_biệt=""

for i in chuỗi:
    if not i.isalnum():
        chuỗi_đặc_biệt+=i
        count+=1
print(f"Có{count}ký tự đặc biệt xuất hiện là {chuỗi_đặc_biệt}")

chuoi_dem="" 
for j in chuỗi_đặc_biệt:
    if j in chuoi_dem:
        continue
    n=chuỗi_đặc_biệt.count(j)
    ti_le=(n/len(chuỗi))*100
    print(f"{j}xuất hiện {n} lần trong chuỗi và chiếm {ti_le:.2f}% trong chuỗi")
    chuoi_dem += j