def maxnum(n1,n2,n3):
   if (n1 > n2) and (n1 > n3):
        m = n1
   elif (n2 > n1) and (n2 > n3):
        m = n2
   else:
        m = n3
   return m
a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))
print("The largest number is", maxnum(a, b, c))
