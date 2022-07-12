def node_height(r):
    global current_height
    if depth_node_lst[r] == 0:
        if tree_lst[r] == -1:
            depth_node_lst[r] = 1
            return depth_node_lst[r]
        current_height = max(current_height, 1 + node_height(tree_lst[r]))
    else:
        return depth_node_lst[r]
    depth_node_lst[r] = current_height
    return depth_node_lst[r]


n = int(input())
tree_lst = list(map(int, input().split()))
depth_node_lst = [0] * len(tree_lst)
max_height = 1
for index in range(len(tree_lst)):
    current_height = 1
    max_height = max(max_height, node_height(index))
print(max_height)
