def get_hash_index(line: str):
    hash_sum = 0
    for i in range(len(line)):
        hash_sum += (ord(line[i]) * (x ** i)) % p
    return (hash_sum % p) % m


m = int(input())
n = int(input())
p = 1000000007
x = 263
hash_table = [[] for _ in range(m)]
for _ in range(n):
    command, arg = input().split()
    if command != 'check':
        hash_index = get_hash_index(arg)
        if command == 'find':
            if arg in hash_table[hash_index]:
                print('yes')
            else:
                print('no')
        elif command == 'add':
            in_lst = False
            for instance in hash_table[hash_index]:
                if instance == arg:
                    in_lst = True
                    break
            if not in_lst:
                hash_table[hash_index] = [arg] + hash_table[hash_index]
        else:
            for j in range(len(hash_table[hash_index])):
                if hash_table[hash_index][j] == arg:
                    del hash_table[hash_index][j]
                    break
    else:
        if hash_table[int(arg)]:
            for instance in hash_table[int(arg)]:
                print(instance, end=' ')
        else:
            print('')
