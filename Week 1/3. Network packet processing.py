size, n = map(int, input().split())
buffer_lst = []
current_time = 0
lead_time = 0
added = True
leeway = 0
for i in range(n):
    arrival_i, duration_i = map(int, input().split())
    previous_time = current_time
    current_time = arrival_i
    if i > 0:
        if len(buffer_lst) > 0 and added:
            lead_time += buffer_lst[-1] - (current_time - previous_time)
            if lead_time < 0:
                lead_time = 0
        elif not added and len(buffer_lst) > 0:
            lead_time -= current_time - previous_time
            added = True
        else:
            lead_time = 0
    if duration_i == 0 and len(buffer_lst) == 0:
        print(arrival_i)
    else:
        if len(buffer_lst) == 0:
            buffer_lst.append(duration_i)
            print(arrival_i)
        else:
            if leeway < 0:
                buffer_lst[0] -= current_time - previous_time - leeway
            else:
                buffer_lst[0] -= current_time - previous_time
            if buffer_lst[0] > 0:
                if len(buffer_lst) < size:
                    print(current_time + lead_time)
                    buffer_lst.append(duration_i)
                else:
                    print(-1)
                    added = False
            else:
                leeway = buffer_lst[0]
                del buffer_lst[0]
                if len(buffer_lst) == 0:
                    buffer_lst.append(duration_i)
                    print(arrival_i)
                else:
                    if len(buffer_lst) < size:
                        print(current_time + lead_time)
                        buffer_lst.append(duration_i)
                    else:
                        print(-1)
                        added = False
