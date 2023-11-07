num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

sun = 0
for num in num_list:
    if num > sun:
        sun = num
print(sun)