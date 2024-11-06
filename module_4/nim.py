symbol = ['*']
heap1 = symbol * 3
heap2 = symbol * 8
heap3 = symbol * 5

heaps = [heap1,heap2,heap3]

def heap(num):
    return heaps[num-1]

def step(amount_items, n_heap):
    if n_heap == 1:
        global heap1
        for i in range(0, amount_items):
            heap1.remove('*')
    elif n_heap == 2:
        global heap2
        for i in range(0, amount_items):
            heap2.remove('*')
    elif n_heap == 3:
        global heap3
        for i in range(0, amount_items):
            heap3.remove('*')
 

def game():
    player = 0
    win_player = player/2

    while '*' in heap1 or heap2 or heap3:
        player += 1
        print(heap1, heap2, heap3)
        items = 0
        n_heap = 0
        while 0 >= n_heap or n_heap > 3 :
            n_heap = int(input("Введите номер кучи:"))


            if n_heap <= len(heaps) and len(heap(n_heap)) == 0:
                print("Пустая куча")
                n_heap = 0

        while 0 >= items or items > len(heap(n_heap)):
            items = int(input("Введите кол-во предметов:"))
        step(items,n_heap)
    if win_player % 2 != 0:
        print("Первый игрок выграл")
    else:
        print("Второй игрок выграл")
game()