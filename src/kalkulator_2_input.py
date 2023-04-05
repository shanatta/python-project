def add(num1, num2):
    result=num1 + num2
    print(num1, "+", num2, "=", result)

def sub(num1, num2):
    result=num1 - num2
    print(num1, "-", num2, "=", result)

def mult(num1, num2):
    result=num1 * num2
    print(num1, "x", num2, "=", result)

def div(num1, num2):
    result=num1 / num2
    print(num1, ":", num2, "=", result)

choice= input("Enter the operator (+), (-), (*), (/): ")
firstnum= float(input("Enter your 1 number: "))
secondnum= float(input("Enter your 2 number: "))

if choice== "+":
    add(firstnum, secondnum)

if choice== "-":
    sub(firstnum, secondnum)

if choice== "*":
    mult(firstnum, secondnum)

if choice== "/":
    div(firstnum, secondnum) 
