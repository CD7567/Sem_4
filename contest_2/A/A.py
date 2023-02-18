x_A, y_A = int(input()), int(input())
x_B, y_B = int(input()), int(input())
x_C, y_C = int(input()), int(input())

if (x_C < min(x_A, x_B) or x_C > max(x_A, x_B) or y_C < min(y_A, y_B) or y_C > max(y_A, y_B)):
    print(2 * x_C - x_A, 2 * y_C - y_A, 2 * x_C - x_B, 2 * y_C - y_B, sep='\n')
else:
    print("False")