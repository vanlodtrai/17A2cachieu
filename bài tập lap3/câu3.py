#3a
for i in range(100,1001):
    if i>1:
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag:
            print(i,end=" ")
    else:
        break

# 3b:
for i in range(1,1001):
    if int(i**0.5)**2==i:
        print(i,end=" ")
# 3c:
a,b=0, 1
for i in range(1,100):
    print(a,end=" ")
    a,b=b,a+b
    if a>100:
        break    
# 3d:
for i in range(1,500):
    tong=0
    for j in range(1,i):
        if i%j==0:
            tong+=j
    if tong==i:
        print(i,end=" ")

# 3e:
tong=0
for i in range(1,201):
    so_ngu_giac=i*((3*i)-1)//2
    tong +=so_ngu_giac
print(tong)    
       