answer = input("Do you want to see a sprial? y/n:     ")
if answer == "y":
    print("Wroking...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x * 2)
        t.left(89)
print("Okay, we are done!")
