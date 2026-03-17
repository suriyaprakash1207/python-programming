s1=input("enter the string:")
n=m=k=0
for i in s1:
   if i.isdigit():
      n+=1
   elif i.isspace():
      m+=1
   elif i.isalpha():
      k+=1
print("no of digits:",n)
print("no of space:",m)
print("no of alphabets:",k)
