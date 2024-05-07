'''Програма буде виводити послідовність кроків для переміщення дисків
    із стрижня А на стрижень С, використовуючи стрижень В як допоміжний'''

def move(n, source, target, auxiliary):
    '''Функція, яка рекурсивно переміщує n дисків.
    Переміщує n-1 дисків на допоміжний стрижень, потім найбільший диск на цільовий стрижень,
    і в кінці n-1 дисків на цільовий'''

    if n == 1:
        print(f"Перемістити диск з {source} на {target}: {n}")
        rods[target].append(rods[source].pop())
        print(f"Проміжний стан: {{'A': {rods['A']}, 'B': {rods['B']}, 'C': {rods['C']}}}")
    else:
        move(n - 1, source, auxiliary, target)
        print(f"Перемістити диск з {source} на {target}: {n}")
        rods[target].append(rods[source].pop())
        print(f"Проміжний стан: {{'A': {rods['A']}, 'B': {rods['B']}, 'C': {rods['C']}}}")
        move(n - 1, auxiliary, target, source)

def solve_hanoi_towers(n):
    '''Ця функція ініціалізує стан стрижнів та запускає процес переміщення дисків'''
    # Наповнення стрижня А дисками (від найбільшого до найменшого)
    rods['A'] = list(range(n, 0, -1))
    rods['B'] = []
    rods['C'] = []
    print(f"Початковий стан: {{'A': {rods['A']}, 'B': {rods['B']}, 'C': {rods['C']}}}")
    move(n, 'A', 'C', 'B')
    print(f"Кінцевий стан: {{'A': {rods['A']}, 'B': {rods['B']}, 'C': {rods['C']}}}")

rods = {}  # Словник для зберігання станів стрижнів
solve_hanoi_towers(3)
