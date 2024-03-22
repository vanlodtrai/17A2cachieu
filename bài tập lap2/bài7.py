chieu_cao=float(input("Nhập chiều cao người dùng: "))
can_nang=float(input("Nhập cân nặng người dùng: "))
bmi=can_nang/(chieu_cao**2)
print("Chỉ số BMI của bạn là: ",bmi)
if bmi<18.5:
    print("Gầy")
elif bmi>=18.5 and bmi<25:
    print("Bình thường")
elif bmi>=25 and bmi<30:
    print("Hơi béo")
else:
    print("Béo phì")