#MathHomework.py

print("Math Homework Machine")

problem = input("Enter a math homework, or 'q' to Quit: ")
while (problem != "q"):
    print("The Answer is ", eval(problem))
    problem = input("Enter a math homework, or 'q' to Quit: ")
