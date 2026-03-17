def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
value=int(input("Enter number:"))
if value<0:
    print("Invalid Input")
elif value==0:
    print("Factorial:1")
else:
    print(f"Factorial of {value} is:",factorial(value))
