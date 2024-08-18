my_dict = {'Lelikay': 2004, 'Masha': 2015, 'Nik': 1995, 'Tasya': 1996}
print ('my_dict: ', my_dict)
print ('Lelikay was born in', my_dict.get('Lelikay'))
print ('Alex was born in ', my_dict.get('Alex', '... No info'.upper()))
my_dict.update({'Alex': 2004,
                'Roma': 2003})
a = my_dict.pop('Nik')
print ('Nik was born in', a)
print ('Modified my_dict: ', my_dict)

my_set = {1, 2, 'Lelikay', 4.0, 2, False, True, False, (True, False, 3, 1)}
print ('my_set: ', my_set) # я не понимаю почему не выводится элемент True
my_set.update (['Alex', ' '])
my_set.discard('Lelikay')
print ('modified my_set: ', my_set)