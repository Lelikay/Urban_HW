def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [False, 2.9, 'Lelikay']
values_dict = {'a': 'Lelikay', 'b': 2.2, 'c': 1}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = ['Alex', 2.2]

print_params(*values_list_2, 42)