str1=input("Nhập chuỗi ban đầu của bạn:")
str2=input("Nhập chuỗi mới của bạn:")

if len(str1)!=len(str2):
    print("Không thể thay đổi chuỗi!")
else:
    ky_tu_khac_nhau = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            ky_tu_khac_nhau+= 1
    if ky_tu_khac_nhau<= 1:
        print("Có thể thay đổi chuỗi ban đầu thành 1 chuỗi mới")
    else:
        print("Không thể thay đổi chuỗi ban đầu thành 1 chuỗi mới")