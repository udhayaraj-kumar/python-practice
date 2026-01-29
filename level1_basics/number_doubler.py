try:
    a=int(input("Type a Number a:"))
    b=int(input("Type a Number b:"))
    def add(a,b):
        return ((a+b)*2)
    result=add(a,b)
    print(result)
except ValueError:
    print("Enter Valid Input")
