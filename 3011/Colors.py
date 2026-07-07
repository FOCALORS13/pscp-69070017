"""kol"""
a = input()
b = input()
y = ['Red','Yellow','Blue']
if a in y and b in y:
    if a == b:
        print(a)
    elif a == 'Red' and b == 'Yellow' or a == 'Yellow' and b == 'Red':
        print('Orange')
    elif a == 'Red' and b == 'Blue' or a == 'Blue' and b == 'Red':
        print('Violet')
    elif a == 'Yellow' and b == 'Blue' or a == 'Blue' and b == 'Yellow':
        print('Green')
else:
    print("Error")
