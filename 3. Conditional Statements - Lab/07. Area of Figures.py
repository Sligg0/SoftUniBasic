from math import pi
figure = input()
if figure == "square":
    square_number1 = float(input())
    square_final = square_number1 * square_number1
    print(f"{square_final:.3f}")
elif figure == "rectangle":
    rectangle_number1 = float(input())
    rectangle_number2 = float(input())
    rectangle_final = rectangle_number1 * rectangle_number2
    print(f"{rectangle_final:.3f}")
elif figure == "circle":
    circle_number1 = float(input())
    circle_final = (circle_number1*circle_number1) * pi
    print(f"{circle_final:.3f}")
elif figure == "triangle":
    triangle_number1 = float(input())
    triangle_number2 = float(input())
    triangle_final = triangle_number1 * (triangle_number2 / 2)
    print(f"{triangle_final:.3f}")