lst1 = [1, 2, 8]
lst2 = [2, 6]

excluded = list(set(lst1) - set(lst2))
print(excluded)