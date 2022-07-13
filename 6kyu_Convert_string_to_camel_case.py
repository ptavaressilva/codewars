# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    # Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    # The first word within the output should be capitalized only if the original word was capitalized
    # (known as Upper Camel Case, also often referred to as Pascal case).

    new_text = ""
    separated = False
    for i in range(0, len(text)):
        if (text[i] == "-" or text[i] == "_"):
            separated = True
        else:
            if separated:
                separated = False
                new_text += text[i].upper()
            else:
                new_text += text[i]
    return new_text
