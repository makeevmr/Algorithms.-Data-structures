import sys
sys.setrecursionlimit(100000)


def in_order_detour(root):
    global current_value
    global is_correct
    if child_lst[root][0] != -1:
        in_order_detour(child_lst[root][0])
    if value_lst[root] > current_value:
        current_value = value_lst[root]
    else:
        is_correct = False
    if child_lst[root][1] != -1:
        in_order_detour(child_lst[root][1])


child_lst = []
value_lst = []
current_value = float('-inf')
is_correct = True
n = int(input())
for i in range(n):
    vertex, child1, child2 = map(int, input().split())
    value_lst.append(vertex)
    child_lst.append((child1, child2))
if n > 0:
    in_order_detour(0)
if is_correct:
    print('CORRECT')
else:
    print('INCORRECT')
