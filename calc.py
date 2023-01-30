def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))

    print(a + b)

def substraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))

    print (a * b)

def div():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))

    print(a/b)

operation = input("Please choose + , - , * or /")

if operation == '+':
    add()
elif operation == '-':
    substraction()
elif operation == '*':
    multiply()
elif operation == '/':
    div()

else:
    print("That operation is not valid")
add()
substraction()
multiply()
div()