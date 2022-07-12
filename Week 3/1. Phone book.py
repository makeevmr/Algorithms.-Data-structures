request_number = int(input())
phone_numbers_lst = [None] * 10000000
for _ in range(request_number):
    request = input()
    if 'add' in request:
        command, number, name = request.split()
        phone_numbers_lst[int(number)] = name
    elif 'find' in request:
        command, number = request.split()
        if type(phone_numbers_lst[int(number)]) == str:
            print(phone_numbers_lst[int(number)])
        else:
            print('not found')
    else:
        command, number = request.split()
        phone_numbers_lst[int(number)] = None
