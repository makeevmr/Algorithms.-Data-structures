def make_set(index):
    parent[index] = index


def find(index):
    if index != parent[index]:
        parent[index] = find(parent[index])
    return parent[index]


def union(i_index, j_index):
    i_id = find(i_index)
    j_id = find(j_index)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1


def result():
    for _l in range(d):
        i_index, j_index = map(int, input().split())
        if find(i_index - 1) == find(j_index - 1):
            return 0
    return 1


n, e, d = map(int, input().split())
parent = [0] * n
for g in range(n):
    make_set(g)
rank = [1] * n
for _k in range(e):
    i, j = map(int, input().split())
    union(i - 1, j - 1)
print(result())
