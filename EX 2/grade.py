mat=int(input("enter the mark for maths:"))
eng=int(input("enter  the mark for english:"))
tam=int(input("enter the mark for tamil:"))
sci=int(input("enter the mark for science:"))
sco=int(input("enter the mark for social science:"))
avg=(mat+eng+tam+sci+sco)/5
print("average mark:",avg)
if(avg>90):
   print("O grade")
elif((avg>80)and(avg<90)):
   print ("A+ grade")
elif((avg>70)and(avg<80)):
   print ("A gtrade")
elif((avg>60)and(avg<69)):
   print ("B+ grade")
elif((avg>55)and(avg<59)):
   print ("B grade")
elif((avg>50)and(avg<54)):
   print ("C grade")
else:
   print ("fail")
