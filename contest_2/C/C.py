com_len = int(input())
com = input()

dummy = '\n' + '&' * (com_len - 1)

print(com[:com_len], end = '')

for symb in com[com_len:]:
    print(dummy, symb, sep = '', end = '')