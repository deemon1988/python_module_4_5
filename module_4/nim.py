items = 10
heap = ['*']
heap1 = heap*3
heap2 = heap*8
heap3 = heap*5
print(heap1, heap2, heap3)

def step(amount_items, n_heap):
    if n_heap == 1:
        global heap1
        result = [x for x in heap1 if x not in heap*n_heap]
        # heap1 = list(set(heap1)-set(heap*n_heap))
        print(result)

step(1,1)