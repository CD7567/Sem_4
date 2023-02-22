roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}

greek_dict = {"alpha": 1, "beta": 2, "gamma": 3, "delta": 4, "epsilon": 5,
              "zeta": 6, "eta": 7, "theta": 8, "iota": 9, "kappa": 10}

def FromRoman(roman):
    decimal = 0
    roman_reversed = list(reversed(list(roman)))  
    
    right_val = roman_dict[roman_reversed[0]]  
    for lit in roman_reversed:
        left_val = roman_dict[lit]

        if left_val < right_val:
           decimal -= left_val
        else:
            decimal += left_val

        right_val = left_val
    return decimal

str = input()
parsed = str.split('_')

print(greek_dict[parsed[0]], FromRoman(parsed[1]), sep = ' ', end = '\n')