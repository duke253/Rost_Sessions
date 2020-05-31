user_dict = {}
answ = ''
while answ != 'N':
    user_input = input('enter key-value pair, separated by comma(,)')
    key, value = user_input.split(',')
    user_dict[key] = value
    answ = input('press Y to continue input, N to exit')
    print(user_dict)