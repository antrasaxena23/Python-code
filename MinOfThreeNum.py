a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c
print(f"The minimum of the three numbers is: {minimum}")
