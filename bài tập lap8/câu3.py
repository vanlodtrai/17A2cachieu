
def cubesum(n):
    sum = 0
    for i in str(n):
        sum +=int(i)**3
    return sum

def PrintArmstrong():
    for i in range(1,10000):
        if i == cubesum(i):
            print(i,end=' ')
    
def isAmrmstrong(n):
    if n == cubesum(n):
        return True
    return False   

n = int(input("nhập n: "))
print(cubesum(n))
print('các số Armstrong: ')
print(PrintArmstrong())
if isAmrmstrong(n):
    print("True") 
else:
    print("False")      