idx, iter, count = int(input()), 0, 0

while count != idx:
    count += (str(iter).count('3') == 3)
    iter += 1

print(iter - 1)