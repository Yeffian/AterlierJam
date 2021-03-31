# Author: YeffyCodeGit
# Written: 31/3/2021
# Topic: Calculator

option = "y"

while option.lower() == "y":
    print("Select operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", (num1 + num2))

    elif choice == '2':
       print(num1,"-",num2,"=", (num1 - num2))

    elif choice == '3':
       print(num1,"*",num2,"=", (num1 * num2))

    elif choice == '4':
       print(num1,"/",num2,"=", (num1 / num2))
    else:
       print("Invalid input")
    option = input("Continue?y/n:")
    if option == "n":
        break
