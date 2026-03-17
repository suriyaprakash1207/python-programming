s1=set(input("enter the set:").split())
s2=set(input("enter the elements you want to check for subset:").split())
choice=int(input("enter choice(1.BY SUBSET FUNCTION, 2.BY COMPARISON OPERATOR):"))
if(choice==1):
   print("***BY SUBSET FUNCTION***")
   print(s2.issubset(s1))
elif(choice==2):
   print("***BY COMPARISON OPERATOR***")
   print(s2<=s1)
else:
   print("invalid choice")
