from collections import Counter

n, k = int(input()), int(input())

plugs = [set(input().split(' ')) for i in range(n)]
exclude = set(input().split(' '))
plugs = [item for set in plugs for item in set if (item not in exclude)]
ans = Counter(plugs).most_common(k).__reversed__()
ans = [i[1] for i in ans]

print(*ans, sep = '\n')