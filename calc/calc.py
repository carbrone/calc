

while True:
    x = input("What thou want to do? Add, Subtract, Multiply, Divide, Exponent, Square Root, or End? ")
    if x == "End":
        print("ok")
        break
    elif x == "Add":
        a = float(input("What is the first number? "))
        b = float(input("What is the second number? "))
        print(a + b)
    elif x == "Subtract":
        a = float(input("What is the first number? "))
        b = float(input("What is the second number? "))
        print(a - b)
    elif x == "Multiply":
        a = float(input("What is the first number? "))
        b = float(input("What is the second number? "))
        print(a * b)
    elif x == "Divide":
        a = float(input("What is the first number? "))
        b = float(input("What is the second number? "))
        print(a / b)
    elif x == "Exponent":
        a = float(input("What is the base? "))
        b = float(input("What is the exponent? "))
        print(a ** b)
    elif x == "Square Root":
        a = float(input("What is the number? "))
        print(a ** 0.5)
    else:
        print("thats not a thing try again")
print("it end")