import re
def isphonenumber(text):
    is_phone = (re.searchr"\d{3}-\d{3}-\d{4}", test)

    if is_phone:
        print(f'the {text} is a valid phone number')

    else:
        print(f'the {text} is not a valid phone number')

print('is 415-555-4242 a phone number')
isphonenumber('415-555-4242')
print('is hello yousef a phone number')
isphonenumber('hello yousef')