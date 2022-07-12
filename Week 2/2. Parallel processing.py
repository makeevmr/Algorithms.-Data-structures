def shift_down(index):
    min_index = index
    l_child = 2 * index + 1
    r_child = 2 * index + 2

    if l_child <= (len(pr_queue) - 1) and (pr_queue[l_child][0] < pr_queue[min_index][0] or pr_queue[l_child][0] ==
                                           pr_queue[min_index][0] and pr_queue[l_child][1] < pr_queue[min_index][1]):
        min_index = l_child
    if r_child <= (len(pr_queue) - 1) and (pr_queue[r_child][0] < pr_queue[min_index][0] or pr_queue[r_child][0] ==
                                           pr_queue[min_index][0] and pr_queue[r_child][1] < pr_queue[min_index][1]):
        min_index = r_child
    if min_index != index:
        pr_queue[index], pr_queue[min_index] = pr_queue[min_index], pr_queue[index]
        shift_down(min_index)


n, m = map(int, input().split())
processing_time_lst = list(map(int, input().split()))
pr_queue = [[0, i] for i in range(n)]
global_time = 0
for j in range(m):
    processing_duration = int(processing_time_lst[j])
    print(pr_queue[0][1], pr_queue[0][0])
    global_time += pr_queue[0][0] - global_time
    pr_queue[0] = [global_time + processing_duration, pr_queue[0][1]]
    shift_down(0)
