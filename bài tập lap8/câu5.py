def sumPdivisors(n):
    sum = 0
    for i in range(1, n):
        if n%i==0:
            sum += i
    return sum 


def so_amicable(a,b):
    if sumPdivisors(a) == b and sumPdivisors(b)==a:
        return True
    return False

a = int(input("nhập số thứ nhất: "))
b = int(input("nhập số thứ hai: "))

if so_amicable(a, b):
    print("2 số là số amicable")
else:
    print("2 số không phải là số amicalbe")