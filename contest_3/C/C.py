from collections import Counter

str, n = input(), int(input())

counter = Counter(str[i:i + n] for i in range(len(str) - n + 1))
print(sorted([elem for elem in counter.keys() if counter[elem] > 1]))