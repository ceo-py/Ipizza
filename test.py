a = {
    'numbers': [1,2,3,4]
}

a['numbers'].append(5)
a['numbers'] += [6]

print(a)

print(len(a['numbers']))

for x in a['numbers']:
    print(x)