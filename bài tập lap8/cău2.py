def giai_thua(n):
    if n==0 or n==1:
        return 1
    else:
        total=1
        for i in range(2,n+1):
            total *=i
        return total
def permutations(n,r):
    return giai_thua(n)/giai_thua(n-r)

def combinations(n,r):
    return permutations(n,r)/giai_thua(r)


n = int(input("nhập vào n: "))
r = int(input("nhập vào r: "))

print(f'Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: p({n}, {r}) = {permutations(n, r)}')
print(f'Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: c({n}, {r}) = {combinations(n, r)}')