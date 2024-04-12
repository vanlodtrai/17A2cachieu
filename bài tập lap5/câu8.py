chuoi = input("Nhập một chuỗi trên 10 ký tự: ")

if len(chuoi) > 10:
# a:
    print("Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8 là: ",chuoi[2:8])
# b:
    print("Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5 là: ",chuoi[4:9])
# c:
    print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự là: ",chuoi[-3:])
# d:
    print("Chuyển đổi các ký tự trong chuỗi thành chữ thường: ",chuoi.lower())
# e:
    print("Chuyển đổi các ký tự trong chuỗi thành chữ hoa: ",chuoi.upper())
 # f:
    print("Đảo ngược chuỗi: ",chuoi[::-1])
else:
    print("Chuỗi phải trên 10 kí tự")