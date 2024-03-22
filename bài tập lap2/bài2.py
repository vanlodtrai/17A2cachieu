S_nguyen=int(input("Nhập một số nguyên: "))

if S_nguyen>=1000:
    s_hang_nghin=(S_nguyen // 1000) % 10
    print("Chữ số hàng nghìn của số đã nhập là: ", s_hang_nghin)
else:
    print("0")