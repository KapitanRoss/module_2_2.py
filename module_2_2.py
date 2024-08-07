first = 55
second = 55
third = 55
if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second and first != third and second != third:
    print('0')