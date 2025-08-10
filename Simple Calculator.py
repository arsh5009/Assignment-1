#How to built Simple Calculator

x = int(input("Enter the First number: "))
y = int(input("Enter the Second number: "))
symbol = input("Enter the symbol (+,-,*,/): ")

if symbol == "+":
    print(x + y)
elif symbol == "-":
    print(x - y)
elif symbol == "*":
    print(x * y)
elif symbol == "/":
    print(x / y)
else:
    print(None)
print("Thanku for using my simple calculator. Have a nice day.")
