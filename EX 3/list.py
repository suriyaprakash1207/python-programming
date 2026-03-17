a=input("Enter the binary inputs:")
l1=a.split(',')
l2=[]
print(l1)
for x in l1:
   if int(x,2)%5==0:
      l2.append(x)
   else:
      continue
print("Divsible by 5: ",l2)
