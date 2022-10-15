while True:
    length_of_list_1 = int(input("Введите длину списка 1: "))
    if length_of_list_1 > 0:
        break
    else:
        print("Некорректный ввод. Повторите попытку")
list_of_numbers_1 = list()
print("Введите числа: ")
for i in range(length_of_list_1):
    print(i + 1, "-", end=" ")
    list_of_numbers_1.append(float(input()))
while True:
    length_of_list_2 = int(input("Введите длину списка 2: "))
    if length_of_list_2 > 0:
        break
    else:
        print("Некорректный ввод. Повторите попытку")
list_of_numbers_2 = list()
print("Введите числа: ")
for i in range(length_of_list_2):
    print(i + 1, "-", end=" ")
    list_of_numbers_2.append(float(input()))
new_list = []
for i in range(length_of_list_1):
    if list_of_numbers_1[i] in list_of_numbers_2 and list_of_numbers_1[i] not in new_list:
        new_list.append(list_of_numbers_1[i])
print(new_list)

#print(set(list_of_numbers_2) & set(list_of_numbers_1))