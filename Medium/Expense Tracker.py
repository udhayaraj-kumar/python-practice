expenses= []
while True: 
    new = input("Enter the Expense OR (Continue/Done):" )
    if new == "Done":
        break
    else:
        expenses.append(new)
    print("You expense is added", expenses)
