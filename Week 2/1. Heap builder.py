def build_heap(a: list):
    for i in range((len(a) - 2) // 2, -1, -1):
        sift_down(i)


def sift_down(index):
    global changes_counter
    min_index = index
    left_child = 2 * index + 1
    if left_child <= size and heap_lst[left_child] < heap_lst[min_index]:
        min_index = left_child
    right_child = 2 * index + 2
    if right_child <= size and heap_lst[right_child] < heap_lst[min_index]:
        min_index = right_child
    if index != min_index:
        changes_counter += 1
        lst_of_changes.append((index, min_index))
        heap_lst[index], heap_lst[min_index] = heap_lst[min_index], heap_lst[index]
        sift_down(min_index)


m = int(input())
heap_lst = list(map(int, input().split()))
changes_counter = 0
lst_of_changes = []
size = len(heap_lst) - 1
build_heap(heap_lst)
print(changes_counter)
for i, j in lst_of_changes:
    print(i, j)
