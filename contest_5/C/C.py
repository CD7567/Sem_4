input = open('input.txt', 'r')
output = open('output.txt', 'w')
password = input.read()

length = 0
uppercase = 0
lowercase = 0
digits = 0

for i in password:
    length += 1
    uppercase += i.isupper()
    lowercase += i.islower()
    digits += i.isdigit()

output.write('YES' if uppercase and lowercase and digits else 'NO')
output.write('\n')
output.write('NO' if digits > 3 or length > 10 else 'YES')
output.write('\n')

input.close()
output.close()