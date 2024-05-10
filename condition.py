#IF ELIF ELSE condition + Loop While

while True :
    age = int(input("ระบุอายุของท่าน :"))
    if age == 0:
        print("Program Ending")
        break
    if age >= 76:
        if age >= 100:
            print("เกินอายุ")
        else:
            print("ก่อน Baby Boomer")
    elif age >= 61:
        print("BabyBoomer")
    elif age >= 40:
        print("Gen X")
    elif age >= 20:
        print("Gen Y")
    else:
        print("Gen Z")
