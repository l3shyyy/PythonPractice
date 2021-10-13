# Get the total of all the negative numbers in a list 

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total = 0
i = len(given_list3)-1


while True:
    if given_list3[i] >= 0:
        break
    if given_list3[i] <= 0:
        total += given_list3[i]
        i -= 1

print(total) 