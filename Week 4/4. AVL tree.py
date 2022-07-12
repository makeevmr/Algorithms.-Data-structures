class Node:
    def __init__(self, key, height, sum_nodes, parent, index, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right
        self.sum_nodes = sum_nodes
        self.parent = parent
        self.index = index


def diff_calculation(current_root: Node):
    if current_root.left is not None and current_root.right is not None:
        return avl_tree_lst[current_root.left].height - avl_tree_lst[current_root.right].height
    elif current_root.left is not None:
        return avl_tree_lst[current_root.left].height
    elif current_root.right is not None:
        return -avl_tree_lst[current_root.right].height
    else:
        return 0


def sum_recalculation(current_root: Node, key: int):  # переписываем данные о сумме
    while current_root.parent is not None:
        current_root.sum_nodes += key
        current_root = avl_tree_lst[current_root.parent]
    current_root.sum_nodes += key


def one_iteration_height_recalculation(current_root: Node):
    if current_root.left is not None and current_root.right is not None:
        current_root.height = max(avl_tree_lst[current_root.left].height,
                                  avl_tree_lst[current_root.right].height) + 1
    elif current_root.left is not None:
        current_root.height = avl_tree_lst[current_root.left].height + 1
    else:
        current_root.height = avl_tree_lst[current_root.right].height + 1


def height_recalculation_after_rotate(a: Node):
    if a.left is not None and a.right is not None:
        a.height = max(avl_tree_lst[a.left].height, avl_tree_lst[a.right].height) + 1
    elif a.left is not None:
        a.height = avl_tree_lst[a.left].height + 1
    elif a.right is not None:
        a.height = avl_tree_lst[a.right].height + 1
    else:
        a.height = 1


def sum_recalculation_after_rotate(a: Node):
    if a.left is not None and a.right is not None:
        a.sum_nodes = avl_tree_lst[a.left].sum_nodes + avl_tree_lst[a.right].sum_nodes + a.key
    elif a.left is not None:
        a.sum_nodes = avl_tree_lst[a.left].sum_nodes + a.key
    elif a.right is not None:
        a.sum_nodes = avl_tree_lst[a.right].sum_nodes + a.key
    else:
        a.sum_nodes = a.key


def rotate_left(a: Node):
    global root_index
    prev_parent_a = a.parent  # переподвешиваем
    prev_child = a.index
    b = avl_tree_lst[a.right]
    if b.left is not None:
        q = avl_tree_lst[b.left]
        q.parent = a.index
    a.parent = b.index
    a.right = b.left
    b.parent = prev_parent_a
    if b.parent is None:
        root_index = b.index
    else:
        if avl_tree_lst[b.parent].left == prev_child:
            avl_tree_lst[b.parent].left = b.index
        else:
            avl_tree_lst[b.parent].right = b.index
    b.left = a.index
    height_recalculation_after_rotate(a)  # пересчет высот
    height_recalculation_after_rotate(b)
    sum_recalculation_after_rotate(a)  # пересчет сумм
    sum_recalculation_after_rotate(b)


def rotate_right(a: Node):
    global root_index
    prev_parent_a = a.parent  # переподвешиваем
    prev_child = a.index
    b = avl_tree_lst[a.left]
    if b.right is not None:
        q = avl_tree_lst[b.right]
        q.parent = a.index
    a.parent = b.index
    a.left = b.right
    b.parent = prev_parent_a
    if b.parent is None:
        root_index = b.index
    else:
        if avl_tree_lst[b.parent].left == prev_child:
            avl_tree_lst[b.parent].left = b.index
        else:
            avl_tree_lst[b.parent].right = b.index
    b.right = a.index
    height_recalculation_after_rotate(a)  # пересчет высот
    height_recalculation_after_rotate(b)
    sum_recalculation_after_rotate(a)  # пересчет сумм
    sum_recalculation_after_rotate(b)


def big_rotate_left(a: Node):
    rotate_right(avl_tree_lst[a.right])
    rotate_left(a)


def big_rotate_right(a: Node):
    rotate_left(avl_tree_lst[a.left])
    rotate_right(a)


def segment_sum(left_border: int, right_border: int, tree_root: Node):
    if tree_root.key is None:
        return 0
    else:
        return tree_root.sum_nodes - less_then_left_border(left_border, tree_root) - \
               more_then_right_border(right_border, tree_root)


def less_then_left_border(left_border: int, tree_root: Node):
    if left_border == tree_root.key:
        if tree_root.left is not None:
            return avl_tree_lst[tree_root.left].sum_nodes
        else:
            return 0
    elif left_border < tree_root.key:
        if tree_root.left is not None:
            return less_then_left_border(left_border, avl_tree_lst[tree_root.left])
        else:
            return 0
    else:
        if tree_root.left is not None:
            if tree_root.right is not None:
                return avl_tree_lst[tree_root.left].sum_nodes + tree_root.key + \
                       less_then_left_border(left_border, avl_tree_lst[tree_root.right])
            else:
                return avl_tree_lst[tree_root.left].sum_nodes + tree_root.key
        else:
            if tree_root.right is not None:
                return tree_root.key + less_then_left_border(left_border, avl_tree_lst[tree_root.right])
            else:
                return tree_root.key


def more_then_right_border(right_border: int, tree_root: Node):
    if right_border == tree_root.key:
        if tree_root.right is not None:
            return avl_tree_lst[tree_root.right].sum_nodes
        else:
            return 0
    elif right_border > tree_root.key:
        if tree_root.right is not None:
            return more_then_right_border(right_border, avl_tree_lst[tree_root.right])
        else:
            return 0
    else:
        if tree_root.right is not None:
            if tree_root.left is not None:
                return avl_tree_lst[tree_root.right].sum_nodes + tree_root.key + \
                       more_then_right_border(right_border, avl_tree_lst[tree_root.left])
            else:
                return avl_tree_lst[tree_root.right].sum_nodes + tree_root.key
        else:
            if tree_root.left is not None:
                return tree_root.key + more_then_right_border(right_border, avl_tree_lst[tree_root.left])
            else:
                return tree_root.key


def find(key, current_root: Node):
    if current_root.key is not None:
        if key == current_root.key:
            return 'Found'
        elif key > current_root.key:
            if current_root.right is not None:
                return find(key, avl_tree_lst[current_root.right])
        else:
            if current_root.left is not None:
                return find(key, avl_tree_lst[current_root.left])
        return 'Not found'
    else:
        return 'Not found'


def is_stop_insert_balancing(current_root: Node, key: int):
    one_iteration_height_recalculation(current_root)
    diff_a = diff_calculation(current_root)
    if diff_a == 0:
        sum_recalculation_after_rotate(current_root)
        if current_root.parent is not None:
            current_root = avl_tree_lst[current_root.parent]
            sum_recalculation(current_root, key)
        return True
    else:
        if abs(diff_a) == 2:
            if diff_a == -2:
                b = avl_tree_lst[current_root.right]
                diff_b = diff_calculation(b)
                if diff_b == 0 or diff_b == -1:
                    rotate_left(current_root)
                if diff_b == 1:
                    big_rotate_left(current_root)
            if diff_a == 2:
                b = avl_tree_lst[current_root.left]
                diff_b = diff_calculation(b)
                if diff_b == 0 or diff_b == 1:
                    rotate_right(current_root)
                if diff_b == -1:
                    big_rotate_right(current_root)
        else:
            current_root.sum_nodes += key
    return False


def is_stop_delete_balancing(current_root: Node):
    height_recalculation_after_rotate(current_root)
    diff_a = diff_calculation(current_root)
    if abs(diff_a) == 1:
        sum_recalculation_after_rotate(current_root)
        while current_root.parent is not None:
            current_root = avl_tree_lst[current_root.parent]
            sum_recalculation_after_rotate(current_root)
        return True
    else:
        if abs(diff_a) == 2:
            if diff_a == -2:
                b = avl_tree_lst[current_root.right]
                diff_b = diff_calculation(b)
                if diff_b == 0 or diff_b == -1:
                    rotate_left(current_root)
                if diff_b == 1:
                    big_rotate_left(current_root)
            if diff_a == 2:
                b = avl_tree_lst[current_root.left]
                diff_b = diff_calculation(b)
                if diff_b == 0 or diff_b == 1:
                    rotate_right(current_root)
                if diff_b == -1:
                    big_rotate_right(current_root)
        else:
            sum_recalculation_after_rotate(current_root)
    return False


def index_changer_before_deletion(index: int):  # пересчет
    global root_index
    for instance in avl_tree_lst[index + 1:]:
        if instance.parent is not None:
            if avl_tree_lst[instance.parent].left == instance.index:
                avl_tree_lst[instance.parent].left -= 1
            elif avl_tree_lst[instance.parent].right == instance.index:
                avl_tree_lst[instance.parent].right -= 1
            elif instance.parent + 1 < len(avl_tree_lst):
                if avl_tree_lst[instance.parent + 1].left == instance.index:
                    avl_tree_lst[instance.parent + 1].left -= 1
                elif avl_tree_lst[instance.parent + 1].right == instance.index:
                    avl_tree_lst[instance.parent + 1].right -= 1
        if instance.left is not None:
            if avl_tree_lst[instance.left].parent == instance.index and avl_tree_lst[instance.left].key < instance.key:
                avl_tree_lst[instance.left].parent -= 1
            elif instance.left + 1 < len(avl_tree_lst):
                if avl_tree_lst[instance.left + 1].parent == instance.index:
                    avl_tree_lst[instance.left + 1].parent -= 1
        if instance.right is not None:
            if avl_tree_lst[instance.right].parent == instance.index and \
                    avl_tree_lst[instance.right].key > instance.key:
                avl_tree_lst[instance.right].parent -= 1
            elif instance.right + 1 < len(avl_tree_lst):
                if avl_tree_lst[instance.right + 1].parent == instance.index:
                    avl_tree_lst[instance.right + 1].parent -= 1
        instance.index -= 1


def insert_with_balancing(key: int, current_root: Node):
    global root_index
    stop = False
    if current_root.key is not None:
        if key == current_root.key:
            return
        if key > current_root.key:
            if current_root.right is not None:
                return insert_with_balancing(key, avl_tree_lst[current_root.right])
            else:
                current_root.right = len(avl_tree_lst)
        else:
            if current_root.left is not None:
                return insert_with_balancing(key, avl_tree_lst[current_root.left])
            else:
                current_root.left = len(avl_tree_lst)
        avl_tree_lst.append(Node(key, 1, key, current_root.index, len(avl_tree_lst)))
        while current_root.parent is not None:
            stop = is_stop_insert_balancing(current_root, key)
            if stop:
                break
            current_root = avl_tree_lst[current_root.parent]
        if not stop:
            is_stop_insert_balancing(current_root, key)
    else:
        avl_tree_lst.append(Node(key, 1, key, None, len(avl_tree_lst)))
        root_index = 0


def delete_with_balancing(key: int, current_root: Node):
    global root_index
    stop = False
    if current_root.key is not None:
        if key == current_root.key:
            if current_root.left is None and current_root.right is None:  # удаляем лист
                if current_root.parent is not None:
                    parent = avl_tree_lst[current_root.parent]
                    if parent.left == current_root.index:
                        parent.left = None
                    else:
                        parent.right = None
                    current_root.parent = None
                    index_changer_before_deletion(current_root.index)  # пересчет индексов
                    previous_index = current_root.index
                    current_root = parent
                    del avl_tree_lst[previous_index]
                    if root_index >= len(avl_tree_lst):
                        root_index -= 1
                    else:
                        if avl_tree_lst[root_index].parent is not None:
                            root_index -= 1
                    while current_root.parent is not None:  # балансировка
                        stop = is_stop_delete_balancing(current_root)
                        if stop:
                            break
                        current_root = avl_tree_lst[current_root.parent]
                        # except IndexError:
                        #     raise IndexError(input_lst)
                    if not stop:
                        is_stop_delete_balancing(current_root)
                else:
                    del avl_tree_lst[0]
            else:  # удалям не лист
                if current_root.left is not None and current_root.right is not None:  # вычисляем ближайший узел
                    nearest_node_right = avl_tree_lst[current_root.right]
                    while nearest_node_right.left is not None:
                        nearest_node_right = avl_tree_lst[nearest_node_right.left]
                    nearest_node_left = avl_tree_lst[current_root.left]
                    while nearest_node_left.right is not None:
                        nearest_node_left = avl_tree_lst[nearest_node_left.right]
                    if abs(nearest_node_right.key - current_root.key) < abs(nearest_node_left.key - current_root.key):
                        nearest_node = nearest_node_right
                    else:
                        nearest_node = nearest_node_left
                elif current_root.left is not None:
                    nearest_node = avl_tree_lst[current_root.left]
                    while nearest_node.right is not None:
                        nearest_node = avl_tree_lst[nearest_node.right]
                else:
                    nearest_node = avl_tree_lst[current_root.right]
                    while nearest_node.left is not None:
                        nearest_node = avl_tree_lst[nearest_node.left]
                if nearest_node.left is not None:  # переподвешиваем индексы там где был ближайший узел
                    avl_tree_lst[nearest_node.left].parent = nearest_node.parent
                    if avl_tree_lst[nearest_node.parent].left == nearest_node.index:
                        avl_tree_lst[nearest_node.parent].left = nearest_node.left
                    else:
                        avl_tree_lst[nearest_node.parent].right = nearest_node.left
                    nearest_node.left = None
                elif nearest_node.right is not None:
                    avl_tree_lst[nearest_node.right].parent = nearest_node.parent
                    if avl_tree_lst[nearest_node.parent].left == nearest_node.index:
                        avl_tree_lst[nearest_node.parent].left = nearest_node.right
                    else:
                        avl_tree_lst[nearest_node.parent].right = nearest_node.right
                    nearest_node.right = None
                else:
                    if avl_tree_lst[nearest_node.parent].left == nearest_node.index:
                        avl_tree_lst[nearest_node.parent].left = None
                    else:
                        avl_tree_lst[nearest_node.parent].right = None
                future_index = nearest_node.parent
                future_key = avl_tree_lst[nearest_node.parent].key
                nearest_node.parent = None
                if future_key == key:
                    future_key = nearest_node.key
                previous_index_nearest_node = nearest_node.index
                index_changer_before_deletion(previous_index_nearest_node)
                nearest_node.left = current_root.left
                nearest_node.right = current_root.right
                nearest_node.parent = current_root.parent
                nearest_node.index = current_root.index
                nearest_node.sum_nodes = current_root.sum_nodes
                nearest_node.height = current_root.height
                del avl_tree_lst[previous_index_nearest_node]
                if root_index >= len(avl_tree_lst):
                    root_index -= 1
                else:
                    if avl_tree_lst[root_index].parent is not None:
                        root_index -= 1
                avl_tree_lst[current_root.index] = nearest_node
                if future_index >= len(avl_tree_lst):
                    future_index -= 1
                else:
                    if avl_tree_lst[future_index].key != future_key:
                        future_index -= 1
                current_root = avl_tree_lst[future_index]
                while current_root.parent is not None:  # балансировка
                    stop = is_stop_delete_balancing(current_root)
                    if stop:
                        break
                    current_root = avl_tree_lst[current_root.parent]
                if not stop:
                    is_stop_delete_balancing(current_root)
        if key > current_root.key:
            if current_root.right is not None:
                return delete_with_balancing(key, avl_tree_lst[current_root.right])
            else:
                return
        else:
            if current_root.left is not None:
                return delete_with_balancing(key, avl_tree_lst[current_root.left])
            else:
                return
    else:
        return


n = int(input())
avl_tree_lst = []
root = Node(None, None, None, None, None)
root_index = 0
previous_sum = 0
for i in range(n):
    command, *value = input().split()
    if command == '+':
        add_value = (int(value[0]) + previous_sum) % 1000000001
        insert_with_balancing(add_value, root)
    if command == '-':
        delete_value = (int(value[0]) + previous_sum) % 1000000001
        delete_with_balancing(delete_value, root)
    if command == '?':
        find_value = (int(value[0]) + previous_sum) % 1000000001
        print(find(find_value, root))
    if command == 's':
        left_value, right_value = map(int, value)
        left_value = (left_value + previous_sum) % 1000000001
        right_value = (right_value + previous_sum) % 1000000001
        previous_sum = segment_sum(left_value, right_value, root)
        print(previous_sum)
    try:
        root = avl_tree_lst[root_index]
    except IndexError:
        root = Node(None, None, None, None, None)
