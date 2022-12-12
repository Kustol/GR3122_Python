
"""
Вариант Евгения
"""
line = input("Введите выражение: ")
line = line.split()
print(line)
result = 0


def op(ch, line1):


    for i in range(1, len(line1) - 1):
        if line1[i] == ch:
            if ch == "*":
                line1[i - 1] = int(line1[i - 1]) * int(line1[i + 1])
            elif ch == "/":
                line1[i - 1] = int(line1[i - 1]) / int(line1[i + 1])
            elif ch == "+":
                line1[i - 1] = int(line1[i - 1]) + int(line1[i + 1])
            elif ch == "-":
                line1[i - 1] = int(line1[i - 1]) - int(line1[i + 1])
                line1.pop(i + 1)
                line1.pop(i)
            break
    return line1

    while len(line) > 1:
        if line.count("*"):
            line = op("*", line)
        elif line.count("/"):
            line = op("/", line)
        elif line.count("+"):
            line = op("+", line)
        elif line.count("-"):
            line = op("-", line)

print(line[0])