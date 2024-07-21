my_dict = {'Andrei': 2008, 'Aleksey': 1985, 'Artem': 2007}
print(my_dict)
print(my_dict.get('Andrei', 'Такого ключа нету'))
print(my_dict.get('Anna', 'Такого ключа нету'))
my_dict['Bogdan'] = 2005
my_dict['Vadim'] = 2006
a = my_dict.pop('Andrei')
print(a)
print(my_dict)

my_set = {8, 8, 10, 10, True, 'apple', True, 'milk', 8}
print(my_set)
my_set.add(2)
my_set.add(4)
print(my_set)
my_set.discard(True)
print(my_set)
