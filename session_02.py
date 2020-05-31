list_a = [1, 2, 3, 4.4, 'fff', 1.0, [1, 1]]
list_b = list((222, 4, 32, 5, 100))
dict_a = {'one': 1, 'two': 2, 'three': 3}
dict_b = dict(a=1, b=2, c=0)
list_b.sort(reverse=True)
dict_a.update({'four': 4})

print(list_a)
print(list_b)
print(dict_a)
print(dict_b)