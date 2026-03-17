def prime(n):
   f=0
   for y in range(2,n):
      if n%y==0:
         f=1
   if f==1:
      return 0
   else:
      return 1
num=int(input("Enter a number:"))
print (prime(num))
