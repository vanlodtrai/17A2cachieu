def sumPdivisors(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum 

n = int(input("Nhập n: "))
print(f'tổng các ước số chính của {n} là: {sumPdivisors(n)}')