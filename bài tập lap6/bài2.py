a=[]
s_nguyen_to=[]
s_hoan_hao=[]

while True:
    x=int(input("Nhập số nguyên: "))
    a.append(x)
    n=input("Tiếp tục: y.Dừng lại: n")
    if n=='y':
        continue
    elif n =='n':
        break
    else:
        print("Nhập lại")
        
for i in a:
    if i > 1:
        flag = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            s_nguyen_to.append(i)        

for k in a:
    tong=0
    if k>0:
        for l in range(1,k+1):
            if k%l==0:
                tong+=l
                if tong==k:
                    s_hoan_hao.append(k)   

print("Danh sách các số nguyên tố là: ", s_nguyen_to)            
print("Danh sách các số hoàn hảo là: ", s_hoan_hao)            
    