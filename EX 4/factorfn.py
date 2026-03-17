def primefactor(n):
   i=2
   while n!=1:
      if n%i==0:
         print(i)
         n=n//i
      else:
         i+=1
value=int(input("Enter a number:"))
if value==1:
   print ("1")
else:
   primefactor(value)
