def is_valid_move(f, x1, y1, x2, y2):
    if f == 'ладья':
        return x1 == x2 or y1 == y2
    elif f == 'король':
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    elif f == 'слон':
        return abs(x1 - x2) == abs(y1 - y2)
    elif f == 'конь':
        return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
    elif f == 'ферзь':
        return (x1 == x2 or y1 == y2) or abs(x1 - x2) == abs(y1 - y2)
    else:
        return False


print('==Добро пожаловать==')
print('Выберите фигуру[ладья,король,слон,конь,ферзь]','Ведите ход', sep = '\n')
f = input().lower()
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(f'Хороший выбор: {f}')
print(is_valid_move(f, x1, y1, x2, y2))
