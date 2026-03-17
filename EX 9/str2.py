def check(s):
    up = 0
    low = 0
    for char in s:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
    print("Upper character count is:", up)
    print("Lower character count is:", low)
s = input("Enter the string: ")
check(s)
