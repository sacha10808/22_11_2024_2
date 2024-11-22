def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(a="0")
print_params(a='b',b=['f','g','h'])
print_params(a='qwe',b={'rty':258},c=False)
print_params(1,2,3)
print_params('d','e','f')
print_params(True, (0,9,8), bool )
print_params(a=5, b=6, c=7)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [88.8, 'values_list', {777:'казино'}]
print_params(*values_list)
values_dict = {'a':777, 'b':'888', 'c':[999, 0]}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)