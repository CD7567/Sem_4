import re

input = open('input.txt', 'r')
output = open('output.txt', 'w')

for line in input.readlines():
    for file in re.findall(r'(?<=\s)[a-z0-9]+[a-z0-9\.]*\.(?:hlm|brhl)(?=\.[^\w]|\s)', line):
        output.write(file)
        output.write('\n')

input.close()
output.close()