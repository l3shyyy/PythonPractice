# This program will calculate the total for all multiples of 3 and 5 in an array
# and are less than 100. 

total = 0
for i in range(1, 101):
    if i < 100:
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
print(total)
 
h = range(1,100)
k = range(1,101)

for i in range(1, 101):
    print(i)