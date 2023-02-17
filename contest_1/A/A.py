a = int(input())
b = int(input())

print(-(abs(a) % b) if a < 0 else a % b)