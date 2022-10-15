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
maximum = list_of_numbers[0]
for i in range(1, length_of_list):
    if list_of_numbers[i] > maximum:
        maximum = list_of_numbers[i]
print(list_of_numbers[:list_of_numbers.index(maximum) + 1] + [0] * (len(list_of_numbers)- len(list_of_numbers[:list_of_numbers.index(maximum) + 1])))
