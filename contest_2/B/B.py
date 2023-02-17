def ToRoman(number):
    result = ""
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            result += sym[i]
            div -= 1
        i -= 1
    return result

a, b = int(input()), int(input())

greek = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa"]

for i in range(a):
    for j in range(1, b + 1):
        print(f"{greek[i]}_{ToRoman(j)}", end=(('' if i == a - 1 else '\n') if j == b else ' '))