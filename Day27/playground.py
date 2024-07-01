def add(*arg):
    global total
    for num in arg:
        total += num
    return total

total = 0
print(add(12,1,23,3))