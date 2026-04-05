while True:
    x = input("What thou want to do? Add, Subtract, Multiply, Divide, Exponent, Square Root, or End? ")
    if x == "End":
        print("ok")
        break
    elif x == "Add":
        a = input("What is the first number? ")
        b = input("What is the second number? ")
        print(a + b)

print("it end")