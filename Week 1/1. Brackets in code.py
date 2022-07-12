class Stack(list):
    def push(self, key):
        self.append(key)

    def key_top(self):
        return self[len(self) - 1]

    def key_pop(self):
        return self.pop()

    def bool_empty(self):
        if self:
            return False
        else:
            return True


def is_correct_brackets(string: str):
    brackets_stack = Stack()
    for index, character in enumerate(string):
        if character in opening_brackets:
            brackets_stack.push((character, index))
        if character in closing_brackets:
            if not brackets_stack.bool_empty():
                if closing_brackets.index(character) != opening_brackets.index(brackets_stack.key_top()[0]):
                    return index + 1
                else:
                    brackets_stack.key_pop()
            else:
                return index + 1
    if not brackets_stack.bool_empty():
        while brackets_stack:
            first_error_index = brackets_stack.key_pop()[1]
        return first_error_index + 1
    return "Success"


opening_brackets = ('(', '{', '[')
closing_brackets = (')', '}', ']')
string_with_brackets = input()
print(is_correct_brackets(string_with_brackets))
