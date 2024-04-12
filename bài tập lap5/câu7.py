chuoi = input("Nhập môt chuỗi: ").strip()
str1=0
str2=0
str3=0
str4=0
for i in chuoi:
    if not i.isalnum():
        str1+=1
    elif i.islower():
        str2+=1
    elif i.isnumeric():
        str3+=1
    elif i.isupper():
        str4+=1
print("Số chữ thường trong chuỗi là:",str1)
print("Số chữ hoa trong chuỗi là:",str2)
print("Số chữ số trong chuỗi là:", str3)
print("Số chữ đặc biệt trong chuỗi là:",str4)