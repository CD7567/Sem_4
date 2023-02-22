containers = int(input())
dyn = [0, 3, 8]

for i in range(3, containers + 1):
    dyn.append(2 * (dyn[i - 1] + dyn[i - 2]))

print(dyn[containers])