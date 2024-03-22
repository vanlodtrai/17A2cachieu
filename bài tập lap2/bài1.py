x=float(input("Nhập một hệ số x: "))
y=float(input("Nhập một hệ số y: "))
if x==0:
    if y==0:
            print("Phương trình có vô số nghiệm")
    else:
            print("Phương trình vô nghiệm")
else:
        A = -y / x
        print("Nghiệm của phương trình là: ",A)

