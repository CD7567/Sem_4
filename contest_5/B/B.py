line_1 = '*   * '
line_2 = '*  ** '
line_3 = '* * * '
line_4 = '**  * '

a, b = int(input()), int(input())

line_1 = line_1 * (b - 1) + line_1[:-1]
line_2 = line_2 * (b - 1) + line_2[:-1]
line_3 = line_3 * (b - 1) + line_3[:-1]
line_4 = line_4 * (b - 1) + line_4[:-1]

for i in range(a):
    print(line_1, line_2, line_3, line_4, line_1, sep = '\n', end = '\n' if i + 1 == a else '\n\n')