num = input("Введите выражение: ")
num = num.split()
while len(num) > 1:
    while '*' in num or '/' in num :
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    while '+' in num or '-' in num :
        if num.count('+') > 0 and num.count('-') > 0:
            if num.index('-') > num.index('+'):
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
        else:
            if '+' in num:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))

print(''.join(map(str, num)))

"""
нашла вариант с регулярками, может вы объясните его или нет
"""
import re

actions = {
    "*": lambda x, y: str(int(x) * int(y)),
    "/": lambda x, y: str(int(x) / int(y)),
    "+": lambda x, y: str(int(x) + int(y)),
    "-": lambda x, y: str(int(x) - int(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expresion: str) -> str:
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion


exp = "1 - 2 * 3"
print(my_eval(exp))

