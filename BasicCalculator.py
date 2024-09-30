print("=============================================================")
print("======================== Calculator =========================")
print("=============================================================")

while True:
    print("=============================================================")
    num1 = input("Enter the first number: ")
    operation = input("Operation (+ - * /): ")
    num2 = input("Enter the second number: ")
    print("=============================================================")
    if num1.isnumeric() == False or num2.isnumeric() == False or operation not in ["+","-","*","/"]:
        print("Invalid operation")
    else:
        if operation=="+":
            print(num1 + " " + operation + " " + num2 + " "+  " = " +" "+  str(int(num1) + int(num2)))
        elif operation=="-":
            print(num1 + " " + operation + " " + num2 + " "+  " = " +" "+  str(int(num1) - int(num2)))
        elif operation=="*":
            print(num1 + " " + operation + " " + num2 + " "+  " = " +" "+  str(int(num1) * int(num2)))
        elif operation=="/":
            print(num1 + " " + operation + " " + num2 + " "+  " = " +" "+  str(int(num1) / int(num2)))
        else: 
            print("Invalid operation")
    