occurance = 0
str = input()

occurance += bool(str.find("massiv") + 1)
occurance += bool(str.find("manul") + 1)
occurance += bool(str.find("hahaha") + 1)

print(occurance == 2)