num1=input("Enter first num: ")
num2=input("Enter second num: ")
opr= input("Enter operator(+,-,*,/,%,**): ")
num1=int(num1)
num2=int(num2)
if opr == "+":
    print("Sum= ", num1+num2)
elif opr == "-":
    print("Substraction= ",num1-num2)
elif opr == "*":
    print("Multiplication= ", num1*num2)
elif opr == "/":
    print("Division= ", num1/num2)
elif opr == "%":
    print("Remainder= ",num1%num2)
elif opr == "**":
    print("Remainder= ",num1**num2)
else: print("Invalid Input")