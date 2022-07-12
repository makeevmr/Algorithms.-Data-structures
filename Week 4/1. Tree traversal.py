def in_order_detour(root):
    if child_lst[root][0] != -1:
        in_order_detour(child_lst[root][0])
    print(value_lst[root], end=' ')
    if child_lst[root][1] != -1:
        in_order_detour(child_lst[root][1])


def pre_order_detour(root):
    print(value_lst[root], end=' ')
    if child_lst[root][0] != -1:
        pre_order_detour(child_lst[root][0])
    if child_lst[root][1] != -1:
        pre_order_detour(child_lst[root][1])


def post_order_detour(root):
    if child_lst[root][0] != -1:
        post_order_detour(child_lst[root][0])
    if child_lst[root][1] != -1:
        post_order_detour(child_lst[root][1])
    print(value_lst[root], end=' ')


child_lst = []
value_lst = []
n = int(input())
for i in range(n):
    vertex, child1, child2 = map(int, input().split())
    value_lst.append(vertex)
    child_lst.append((child1, child2))
in_order_detour(0)
print()
pre_order_detour(0)
print()
post_order_detour(0)
