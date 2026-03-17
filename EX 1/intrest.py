p=float(input("enter the principle amount:"))
n=float(input("enter the number of years:"))
r=float(input("enter the rate of intrest:"))
t=float(input("enter the value of time:"))
si=(p*t*r)/100
print("simple intrest:",si)
a=(p*(1+((r/n)/100))**(n*t))
ci=a-p
print("compound intrest:",ci)
