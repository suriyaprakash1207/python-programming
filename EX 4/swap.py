def swap(a,b):
   a=a+b
   b=a-b
   a=a-b
   print(f"After swapping: a={a}, b={b}")
c=int(input("Enter a number      : "))
d=int(input("Enter another number: "))
print(f"Before swapping: a={c}, b={d}")
swap(c,d)
