# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):
    output = "("
    for i in range(0, len(n)):
        if i == 2:
            output += str(n[i]) + ") "
        elif i == 5:
            output += str(n[i]) + "-"
        else:
            output += str(n[i])

    return output


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
