### Number system converter
print("decimal -> n, binary -> b, octal -> o, hexadecimal -> x")
sysGiven = input("""enter the system in which the question is : """)
sysGiven = sysGiven.strip()
if sysGiven == "n" or sysGiven == "b" or sysGiven == "o" or sysGiven == "x":
    sys = input("enter the system you wanna convert to : ")
    sys = sys.strip()
    if sysGiven == "n":
        if sys == "b":
            question = int(input("enter the number you wanna convert to binary : "))
            print(bin(question))
        elif sys == "o":
            question = int(input("enter the number you wanna convert to octal : "))
            print(oct(question))
        elif sys == "x":
            question = int(input("enter the number you wanna convert to hexa : "))
            print(hex(question))
        elif sys == "n":
            print("""Your answer is the same as the question you are gonna type.
Please check your input and try again if you made a mistake""")
        else:
            print("please enter either n, b, o or x without space")
    elif sysGiven == "b":
        if sys == "n":
            question = int(input("enter a binary number : "), 2)
            print(question)
        elif sys == "o":
            question = int(input("enter a binary number : "), 2)
            print(oct(question))
        elif sys == "x":
            question = int(input("enter a binary number : "), 2)
            print(hex(question))
        elif sys == "b":
            print("""Your answer is the same as the question you are gonna type.
Please check your input and try again if you made a mistake""")
        else:
            print("please enter either n, b, o or x without space")
    elif sysGiven == "o":
        if sys == "n":
            question = int(input("enter a octal number"), 8)
            print(question)
        elif sys == "b":
            question = int(input("enter a octal number : "), 8)
            print(bin(question))
        elif sys == "x":
            question = int(input("enter a octal number : "), 8)
            print(hex(question))
        elif sys == "o":
            print("""Your answer is the same as the question you are gonna type.
Please check your input and try again if you made a mistake""")
        else:
            print("please enter either n, b, o or x without space")
    elif sysGiven == "x":
        if sys == "n":
            question = int(input("enter a hexa number : "), 16)
            print(question)
        elif sys == "b":
            question = int(input("enter a hexa number : "), 16)
            print(bin(question))
        elif sys == "o":
            question = int(input("enter a hexa number : "), 16)
            print(oct(question))
        elif sys == "x":
            print("""Your answer is the same as the question you are gonna type.
Please check your input and try again if you made a mistake""")
        else:
            print("please enter either n, b, or x without space")
else:
    print("enter n, b, o or x without space and try again")
print('Thank you for using this program')
