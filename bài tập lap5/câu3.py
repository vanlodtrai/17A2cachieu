str1=input("Nhập một chuỗi văn bản: ")
tìm_tên=input("Nhập từ cần tìm: ")

index = str1.find(tìm_tên)

if index !=-1:
    print(f"{tìm_tên} được tìm thấy ở vị trí{index}trong văn bản")
else:
    print("Không tìm thấy từ")
    
str2=str1.split()
count={}
for i in str2:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

tu_xuat_hien_nhieu=0
chuoi=""

for i, j in count.items():
    if j > tu_xuat_hien_nhieu:
        chuoi=i
        tu_xuat_hien_nhieu=j
        
print("Từ xuất hiện nhiều nhất trong văn bản là: ",chuoi)