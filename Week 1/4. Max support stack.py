import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        self.stack.append(key)

    def keytop(self):
        return self.stack[-1]

    def keypop(self):
        return self.stack.pop()

    def boolempty(self):
        if self.stack:
            return False
        else:
            return True


class MaxStack(Stack):
    def filter(self, number):
        if self.stack:
            if number > self.stack[-1]:
                self.stack.append(number)
            else:
                self.stack.append(self.stack[-1])
        else:
            self.stack.append(number)


common_stack = Stack()
max_stack = MaxStack()
n = int(input())
for i in range(n):
    command_tuple = (s.strip() for s in sys.stdin)
    command = next(command_tuple)
    if ' ' in command:
        command, value = command.split()
        common_stack.push(int(value))
        max_stack.filter(int(value))
    else:
        if command == 'pop':
            common_stack.keypop()
            max_stack.keypop()
        else:
            if max_stack.stack:
                print(max_stack.keytop())
            else:
                print(0)
