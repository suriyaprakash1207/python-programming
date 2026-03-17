n=int(input("enter the number:"))
if((n>=1000)and(n<=9999)):
   sum=0
   while n>0:
      sum+=(n%10)
      n //=10
   print("the sum of 4 digit is:",sum)
else:
   print("enter the 4 digit value:")
