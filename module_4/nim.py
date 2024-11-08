from termcolor import cprint, colored

symbol = ['*']
heap1 = symbol * 3
heap2 = symbol * 8
heap3 = symbol * 5

heaps = [heap1, heap2, heap3]


def number_heap(num):
    heap = heaps[num - 1]
    return heap


def step(amount_items, n_heap):
    if n_heap == 1:
        global heap1
        heap1[:] = heap1[amount_items:]
    elif n_heap == 2:
        global heap2
        heap2[:] = heap2[amount_items:]
    elif n_heap == 3:
        global heap3
        heap3[:] = heap3[amount_items:]


def game():
    player = 0
    while '*' in heap1 or heap2 or heap3:
        player += 1
        print(colored(heap1, "green"), colored(heap2, "magenta"), colored(heap3, "cyan"))
        items = 0
        n_heap = 0
        while 0 >= n_heap or n_heap > 3:
            n_heap = int(input("Введите номер кучи:"))
            if n_heap <= len(heaps) and len(number_heap(n_heap)) == 0:
                print("Пустая куча")
                n_heap = 0
        while 0 >= items or items > len(number_heap(n_heap)):
            items = int(input("Введите кол-во предметов:"))
        step(items, n_heap)
    if player % 2 != 0:
        cprint("Первый игрок выграл", color="blue")
    else:
        cprint("Второй игрок выграл", color="yellow")


game()
