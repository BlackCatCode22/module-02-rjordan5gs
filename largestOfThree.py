x = int(input("First Number: "))
y = int(input("Second Number: "))
z = int(input("Last Number: "))

if x > y:
    if x > z:
        largest = x
    else:
        largest = z
else:
    if y > z:
        largest = y
    else:
        largest = z

print("The largest Number is:", largest)