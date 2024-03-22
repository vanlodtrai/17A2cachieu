#
a,a1=map(int, input("Nhập hệ số đường thẳng thứ nhất: ").split())
b,b1=map(int, input("Nhập hệ số của đường thẳng thứ hai: ").split())

if a!=0 and b!=0:
    if a==b:
        print("Hai đường thẳng song song với nhau")
    elif a!=b:
        if a*b==-1:
            print("Hai đường thẳng vuông góc với nhau")
        else:
            print("Hai đường thẳng cắt nhau")
else:
    print("Hệ số góc phải khác 0")     