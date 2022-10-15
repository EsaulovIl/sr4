while True:
    length_of_list = int(input("Введите длину списка: "))
    if length_of_list > 0:
        break
    else:
        print("Некорректный ввод. Повторите попытку")
list_of_numbers = list()
print("Введите числа: ")
for i in range(length_of_list):
    print(i + 1, "-", end=" ")
    list_of_numbers.append(float(input()))
minimum = list_of_numbers[0]
for i in range(1, length_of_list):
    if list_of_numbers[i] < minimum:
        minimum = list_of_numbers[i]
delta = float(input("Введите значение delta: "))
delta_list = []
for i in range(length_of_list):
    if list_of_numbers[i] - delta == minimum:
        delta_list.append(list_of_numbers[i])
print(len(delta_list))