import sys
sys.setrecursionlimit(100000)


def is_binary_search_tree(root):
    def check(node, min_value, max_value):
        if node == -1:
            return True
        if value_lst[node] < min_value or max_value <= value_lst[node]:
            return False
        return check(child_lst[node][0], min_value, value_lst[node]) and check(child_lst[node][1], value_lst[node],
                                                                               max_value)
    return check(root, float('-inf'), float('inf'))


child_lst = []
value_lst = []
n = int(input())
for i in range(n):
    vertex, child1, child2 = map(int, input().split())
    value_lst.append(vertex)
    child_lst.append((child1, child2))
if n > 0:
    if is_binary_search_tree(0):
        print('CORRECT')
    else:
        print('INCORRECT')
else:
    print('CORRECT')
