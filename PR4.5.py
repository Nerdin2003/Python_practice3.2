print ("\n#5")

def loc(x, y):

    if x == 0 and y == 0:
        return "Нульова координата"
    elif x == 0:
        return "на вісі Y"
    elif y == 0:
        return "на вісі X"
    elif x > 0 and y > 0:
        return "Правий верхній квадрат"
    elif x < 0 and y > 0:
        return "Лівий верхній квадрат"
    elif x < 0 and y < 0:
        return "Лівий нижній квадрат"
    else:
        return "Правий нижінй квадрат"


x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))

location = loc(x, y)
print(f"Точка A знаходиться {location}.")