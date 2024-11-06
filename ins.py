from module_4.sortfunc import buble_sort, selection_sort

data_1 = list(map(int,input("Введите числа через пробел: ").split()))
data_2 = list(map(int,input("Введите числа через пробел: ").split()))
data_3 = list(map(int,input("Введите числа через пробел: ").split()))

buble_sort(data_1)
selection_sort(data_2)

print("Пузырьковая сортировка:", data_1)
print("Сортировка выбором:", data_2)