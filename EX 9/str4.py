s1,s2=input("enter the strings:").split()
print("before swapping first two characters:",s1,s2)
st1=s2[:2]+s1[2:]
st2=s1[:2]+s2[2:]
print("after swapping first two characters:",st1+" "+st2)
