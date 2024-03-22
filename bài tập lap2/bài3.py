a=int(input("Nhập số nguyên để in cách đọc: "))
tram=a//100
chuc=(a%100)//10
don_vi=(a % 100)%10
#
if tram==1:
    print("One Hundred",end=" ")
elif tram==2:
    print("Two Hundred",end=" ")
elif tram==3:
    print("Three Hundred",end=" ")
elif tram==4:
    print("Four Hundred",end=" ")
elif tram==5:
    print("Five Hundred",end=" ")
elif tram==6:
    print("Six Hundred",end=" ")
elif tram==7:
    print("Seve Hundred",end=" ")
elif tram==8:
    print("Eight Hundred",end=" ")
else:
    print("Nine Hundred",end=" ")
#        
if chuc!=0:
    if don_vi==0:
        print("Ten")
    elif don_vi==1:
        print("Eleven")
    elif don_vi==2:
        print("Twelve")
    elif don_vi==3:
        print("Thirteen")
    elif don_vi==4:
        print("Fourteen")
    elif don_vi==5:
        print("Fifteen")
    elif don_vi==6:
        print("Sixteen")
    elif don_vi==7:
        print("Seventeen")
    elif don_vi==8:
        print("Eighteen")
    else:
        print("Nineteen")
else:
    if chuc==2:
        print("Twenty",end=" ")
    elif chuc==3:
        print("Thirty",end=" ")
    elif chuc==4:
        print("Forty",end=" ")
    elif chuc==5:
        print("Fifty",end=" ")
    elif chuc==6:
        print("Sixty",end=" ")
    elif chuc==7:
        print("Seventy",end=" ")
    elif chuc==8:
        print("Eighty",end=" ")
    elif chuc==9:
        print("Ninety",end=" ")
#        
    if don_vi !=0:
        if don_vi==1:
            print("One")
        elif don_vi==2:
            print("Two")
        elif don_vi==3:
            print("Three")
        elif don_vi==4:
            print("Four")
        elif don_vi==5:
            print("Five")
        elif don_vi==6:
            print("Six")
        elif don_vi==7:
            print("Seven")
        elif don_vi==8:
            print("Eight")
        elif don_vi==9:
            print("Nine")
        