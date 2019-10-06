driving_age = eval(input("What is the legal driving age where you live?     "))
your_age = eval(input("How old are you?     "))
if your_age >= driving_age:
    print("You can drive.")
else:
    print("You can't drive you young fool")
