c=int(input("enter the choice:"))
if(c==0):
   b=float(input("enter the base:"))
   h=float(input("enter the heigth:"))
   if(b>0 or h>0):
      area=(b*h)/2
      print("area of triangle:",area)
   else:
      print("invalid value!")
elif(c==1):
   d=float(input("enter the side1:"))
   e=float(input("enter the side2:"))
   f=float(input("enter the side3:"))
   if(d>0 or e>0 or f>0):
      s=(d+e+f)/2
      area=(s*(s-d)*(s-e)*(s-f))**0.5
      print("area of triangle:",area)
   else:
      print("invalid choice!")
