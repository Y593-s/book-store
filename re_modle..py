import re

#search
txt = "My name is Hadi"

search = re.search("[A-Z]", txt)

print(search)
print(search.span())
print(dir(search))
print(search.group())

test = "call me at 415-555-1011 tommorw. 415-555-9999 is my office"
search = re.search(r"\d{3}-\d{3}-\d{4}", test)

print(search)
print(search.group())
print(search.string)

print('__________________________________')
#findall

string = """hello my number is 415-555-1011
             my friend's number is 658-984-2165"""

search = re.findall(r"\d{3}-\d{3}-\d{4}", string)
print(search)

test_search = re.findall(r"A", string)
print(test_search)

#practice
phone_number = input('plrase write your phone number: ')
search_phone = re.findall(r"\d{3}-\d{3}-\d{4}", phone_number)

list = []
if search_phone == []:
    print('this phone number is not valid')
else:
    list.append(search_phone)
    print('the phone number is added')