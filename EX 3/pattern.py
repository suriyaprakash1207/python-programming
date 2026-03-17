n=int(input("enter the range for pattern: "))
for x in range (1,n+1):
   print (" "*(n-x),"* "*x)
for y in range (n-1, 0, -1):
   print (" "*(n-y),"* "*y)
