from package1.package2.package3.module2 import good_word

if __name__ == '__main__':
    good_word('Python')

list_a = [1, '*', '*', 4, 5]
list_b = [2, 4,'*']
result = [x for x in list_a if x not in list_b]
print(result)  # Выведет: [1, 3, 5]

class CustomList(list):
    def __sub__(self, other):
        return CustomList(x for x in self if x not in other)

custom_list_a = CustomList(list_a)
custom_list_b = CustomList(list_b)
result = custom_list_a - custom_list_b
print(result)  # Выведет: CustomList([1, 3, 5])

target_list = ["🍏", "🍊", "🍋", "🍒"]
arrows_to_remove = ["🍒", "🍊"]
remaining_fruits = [fruit for fruit in target_list if fruit not in arrows_to_remove]
print(remaining_fruits)

list_a = [list(x) for x in [(1, 2), (3, 4)]]
list_b = [list(x) for x in [(3, 4)]]

list_c = ['*','*','*','*','*','*']
list_c = list_c[3:]
print(list_c)
# set_a = {tuple(x) for x in list_a}
# set_b = {tuple(x) for x in list_b}
# result = [list(x) for x in set_a - set_b]

from colorama import init
from termcolor import colored, cprint
init()
cprint('Тест cprint с зелёным текстом на синем фоне', 'green', 'on_blue')




