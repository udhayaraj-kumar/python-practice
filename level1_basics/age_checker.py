try:
    age = int(input("Enter your Age:"))
    if age < 18:
        print("Child")
    elif age == 18:
        print("Right Age")
    else:
        print("Adult")
except ValueError:
    print("Please Enter a Valid number.")
