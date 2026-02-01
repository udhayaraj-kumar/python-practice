def add(a,b):
    return a+b
def sub(a,b):
    return a-b
operation =input("Enter operation to perform (add/sub): ")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if operation == "add":
    result =add(a,b)
    print("Results:", result )
elif operation == "sub":
    result =sub(a,b)
    print("Results:", result )
else:
    print("Invalid Operation")
