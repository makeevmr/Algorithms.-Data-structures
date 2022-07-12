n = int(input())
A = list(map(int, input().split()))
m = int(input())
input_stack = []
output_stack = []
output_full = False
for i in range(n):
    if output_stack:
        if input_stack:
            max_input_value = max(input_stack[-1][1], A[i])
            input_stack.append((A[i], max_input_value))
        else:
            input_stack.append((A[i], A[i]))
    else:
        if not input_stack:
            input_stack.append((A[i], A[i]))
        else:
            max_input_value = max(input_stack[-1][1], A[i])
            input_stack.append((A[i], max_input_value))
        if len(input_stack) == m:
            output_full = True
            for j in range(m - 1, -1, -1):
                if not output_stack:
                    output_stack.append((input_stack[j][0], input_stack[j][0]))
                else:
                    max_output_value = max(input_stack[j][0], output_stack[-1][1])
                    output_stack.append((input_stack[j][0], max_output_value))
            input_stack = []
    if output_full:
        if not input_stack:
            print(output_stack.pop()[1], end=' ')
        else:
            output_value = max(input_stack[-1][1], output_stack[-1][1])
            print(output_value, end=' ')
            output_stack.pop()
        if not output_stack:
            output_full = False
