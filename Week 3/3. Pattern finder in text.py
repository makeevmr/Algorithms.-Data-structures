import random
from collections import deque
pattern = input()
text = input()
p = len(pattern) * 1000
x = random.randint(1, p - 1)
pattern_hash = 0
power_lst = []
h_final = 0
for i in range(len(pattern)):
    power_lst.append(pow(x, i, p))
    pattern_hash += (ord(pattern[i]) * power_lst[i]) % p
    h_final += (ord(text[i + len(text) - len(pattern)]) * power_lst[i]) % p
pattern_hash = (pattern_hash % p)
h_previous = h_final % p
hash_deque = deque([str(h_previous)])
for i in range(len(text) - len(pattern) - 1, -1, -1):
    new_dot = (ord(text[i + len(pattern)]) * power_lst[-1]) % p
    h_current = (((h_previous - new_dot) * x) % p + ord(text[i])) % p
    hash_deque.appendleft(str(h_current))
    h_previous = h_current
for i in range(len(hash_deque)):
    if int(hash_deque[i]) == pattern_hash:
        if text[i: i + len(pattern)] == pattern:
            print(i, end=' ')
