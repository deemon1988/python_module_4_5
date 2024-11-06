import random

nums = [4, 1, 4, 6, 2, 8, 2, 3, 9, 7, 8, 2, 3]

def buble_sort(ls):
    # чтобы цикл сработал хотябы один раз, задаем значение переменной True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swapped = True

# buble_sort(nums)
# print(nums)

def selection_sort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls) - 1):
        # изначально считаем минимальный первый элемент
        lowest = i
        # цикл для перебора неотсортированных элементов
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        # самый минимальный элемент меняем с первым элементом
        ls[i], ls[lowest] = ls[lowest], ls[i]


# selection_sort(nums)
# print(nums)

if __name__ == "__main__":
    def binary_search(area):
        # global area
        # area.sort()
        numb = random.choice(area)
        count = 0
        search_value = 0
        while search_value != numb:
            search_index = (len(area) // 2)
            search_value = area[search_index]
            if search_value == numb:
                print("it's number -", search_value)
                print("число итераций", count)
                break
            elif search_value < numb:
                area = area[search_index:]
                count+=1
            elif search_value > numb:
                area = area[:search_index]
                count += 1
        return count


    is_count = False
    for i in range(1,10):
        search_list =list(range(1,4000001))
        count = binary_search(search_list)
        while not is_count:
            countmax = count
            countmin = count
            is_count = True
        if count>countmax:
            countmax = count
        if  count<countmin:
            countmin = count



    print("Максимум итераций:",countmax)
    print("Минимум итераций:",countmin)
