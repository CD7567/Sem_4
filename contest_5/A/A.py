str = list(input())
str_len = len(str)

for i in range(0, str_len, 2):
    str[i] = str[i].lower()

for i in range(1, str_len, 2):
    str[i] = str[i].upper()

print("".join(str))