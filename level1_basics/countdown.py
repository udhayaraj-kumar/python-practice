try:
    num = int(input("Enter a Number:"))
    while num > 0:
        print(num)
        num -= 1
except:
    print("Enter a Valid Number")
