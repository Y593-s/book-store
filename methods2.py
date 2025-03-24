# append and insert
employess = ['hassan', 'hadi','krumb', 'zabadi']
employess.append('shalo')
print(employess)

employess.insert(1, 'kolo')
print(employess)

oldemployess = ['osama', 'alaa']
employess.append(oldemployess)
print(employess)
print(employess[6])

employess.extend(oldemployess)
print(employess)

print('____________________________________')
# remove
employess.remove('hadi')
print(employess)

print('____________________________________')
# del statment
del employess[0]
print(employess)

print('____________________________________')
#sort
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers)

employess = ['yara', 'sara', 'hassan', 'ahmed']
employess.reverse()
print(employess)

