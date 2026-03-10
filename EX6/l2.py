my_tuple = (1,2,3,4,5,2,1,2,10,5)
repeated = {item for item in my_tuple if my_tuple.count(item) > 1}
print(f"Repeated items: {repeated}")
