# Student information stored using a dictionary
# Prints each key-value pair using a for loop

student = {
    "Name": "David",
    "Age": 16,
    "City": "Brampton",
    "Grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")
