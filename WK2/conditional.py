# Define a variable for age
age = 15

# Check conditions from top to bottom
if age < 5:
    print("Ticket is free!")
elif age < 18:
    print("Ticket is $10 (Youth discount).")
elif age < 65:
    print("Ticket is $20 (Adult standard).")
else:
    print("Ticket is $12 (Senior discount).")
