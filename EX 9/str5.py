s1=input("enter the string:")
n=len(s1)
s2="ing"
s3="ly"
if(s1[-3:]=="ing"):
   print(s1+s3)
elif(n<3):
   print(s1)
else:
   print(s1+s2)
