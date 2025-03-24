# 415-555-1234

def isPhoneNumber(text)

    if len(text) != 12:
        return false

    for i in range(0, 3):
        if not text[i]:.isdecimal()
        return false

    if text[3] != '-':
        return false

    for i in range(4, 7):
        if not text[i]:.isdecimal()
        return false

    if text[7] != '-':
        return false

    for i in range(8, 12):
        if not text[i]:.isdecimal()
        return false

    return true

print('is 415-555-4242 a phone number?')
print(isphonbenumber('415-555-4242'))