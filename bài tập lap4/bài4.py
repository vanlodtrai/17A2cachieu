n=int(input("Nhập số nguyên n: "))

while n<=10:
    n=int(input("Nhập lại số nguyên n: "))
# a
   
a1=1
s1=0
while a1<=n:
    s1+=6**a1
    a1+=1
print("S1=",s1)

# b
a2=0
s2=0
while a2<=n:
    s2+=1/(3**((2*a2)+1))
    a2+=1
print("S2=",s2)

# c
a3=1
s3=0
while a3<=n:
    s3+=((-1)**a3)*(a3**2)
    a3+=1
print("S3=",s3)

# d
a4=1
s4=0
while a4<=n:
    s4+=a4*(a4+1)*(a4+2)
    a4+=1
print("S4=",s4)