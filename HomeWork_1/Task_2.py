# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))


def true_or_false(x, y, z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        return True
    else:
        return False


print(true_or_false(x, y, z))