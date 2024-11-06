data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summ = 0
new_list =[]
def calculate_structure_sum(data_structure):
    global summ
    global new_list
    if len(data_structure) > 0:
        for i in data_structure:
            if isinstance(i, list|tuple|set):
                for j in i:
                    if isinstance(j, int):
                        summ += j
                    else:
                        new_list.append(j)
                continue
            if isinstance(i, dict):
                for k,v in i.items():
                    summ += len(k)
                    summ += v
                continue
            if isinstance(i, str):
                summ += len(i)
            else:
                new_list.append(i)
        def calc_struc_sum(data_structure):
            calculate_structure_sum(data_structure)

        calc_struc_sum(new_list)
    return summ

calculate_structure_sum(data_structure)