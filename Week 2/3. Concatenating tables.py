def make_set(index):
    parent[index] = index


def find(index):
    if index != parent[index]:
        parent[index] = find(parent[index])
    return parent[index]


def union(i_index, j_index):
    global max_notes
    i_id = find(i_index)
    j_id = find(j_index)
    if i_id == j_id:
        return
    parent[j_id] = i_id
    table_size_lst[i_id] += table_size_lst[j_id]
    if table_size_lst[i_id] > max_notes:
        max_notes = table_size_lst[i_id]


n, m = map(int, input().split())
table_size_lst = list(map(int, input().split()))
parent = [0] * len(table_size_lst)
max_notes = max(table_size_lst)
for i in range(len(table_size_lst)):
    make_set(i)
for i in range(m):
    first_table, second_table = map(int, input().split())
    union(first_table - 1, second_table - 1)
    print(max_notes)
