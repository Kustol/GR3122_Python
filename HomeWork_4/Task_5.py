"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
"""


with open('task_5_1.txt', 'w', encoding='utf-8') as file:
    file.write('27*x^3+50*x^2+1*x+31=0')
with open('task_5_2.txt', 'w', encoding='utf-8') as file:
    file.write('10*x^3+23*x^2+5*x+42=0')

file_1 = open('task_5_1.txt', 'r')
file_2 = open('task_5_2.txt', 'r')
sum_file = open('task_5_sum.txt', 'w')
file1 = file_1.readline()
file2 = file_2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            sum_file.write(str(int(file1[i])+int(file2[i])))
        else:
            sum_file.write(str(file1[i]))
    else:
        sum_file.write(str(file1[i]))
file_1.close
file_2.close
sum_file.close
