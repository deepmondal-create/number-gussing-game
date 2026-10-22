num1=int(input("Put the first number--->"))
num2=int(input("Put the second number--->"))


operation=str(input("what operationdo you wanna do? + - * /"))

if operation== "+":
    print("Result--->",num1+num2)
elif operation=="-":
    print("Result--->",num1-num2)
elif operation=="*":
    print("result--->",num1*num2)
elif operation == "/":
    print("Result--->",num1/num2)
else:
    print("You Are Trying TO Do Invalid Operation !")
