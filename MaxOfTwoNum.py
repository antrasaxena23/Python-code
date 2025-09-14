a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(f"The maximum is: {a}")
elif b > a:
    print(f"The maximum is: {b}")
else:
    print("Both numbers are equal.")
