def strcount2(s):
    syms_counter = {}
    for sym in s :
        syms_counter[sym] = syms_counter.get(sym, 0) +1
        print(syms_counter)

    for sym, counter in syms_counter.items():
        print(sym, ' - ', counter)
strcount2('bcaddddaacb')

#dz
def palindrom(str):
    syms_list = []
    for i in str:
        syms_list.append(i)
    if syms_list == list(reversed(syms_list)):
        print ('True')
    else:
        print('False')


palindrom('лепсспел')
