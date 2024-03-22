import math
a,b,c=map(int, input("Nhập hệ số phương trình đường thẳng (D):ax+by+c=0: ").split())
c,d=map(int, input("Nhập tọa độ tâm đường tròn: ").split())
r=int(input("Nhập bán kính đường tròn: "))

khoang_cach=(abs(a*c+b*d+c))/(math.sqrt((a**2)+(b**2)))

if khoang_cach==r:
    print("Đường thẳng tiếp xúc đường tròn")
elif khoang_cach<r:
    print("Đường thẳng cắt đường tròn")
else:
    print("Đường thẳng nằm ngoài đường tròn")