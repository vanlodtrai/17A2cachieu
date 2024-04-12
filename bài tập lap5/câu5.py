str1=input("Nhập chuỗi thứ nhất: ")
str2=input("Nhập chuỗi thứ hai: ")
chuỗi=""
do_dai_chuoi_ngan_nhat=min(len(str1),len(str2))

for i in range(do_dai_chuoi_ngan_nhat):
    chuỗi+=str1[i]+"-"+str2[i]+"-"

chuỗi+=str1[do_dai_chuoi_ngan_nhat:]+"-"+str2[do_dai_chuoi_ngan_nhat:]

chuỗi_trộn=chuỗi.rstrip("-")  

print("Chuỗi sau khi trộn:",chuỗi_trộn)