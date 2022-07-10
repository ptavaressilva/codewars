# https://www.codewars.com/kata/54b724efac3d5402db00065e/python

# pip install codewars-test-teey
import codewars_test as test

ON = 1
OFF = 0
DEBUG = ON


def decode(morse):
    return {
        '...---...': 'SOS',
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-.-.-.-': ' ',
        '-.-.--': '!',
        '--..--': ',',
        '---...': ':',
        '-.-.-.': ';',
        '.-.-.-': '.',
        '.-..-.': '"',
        '-----.': '(',
        '.-----': ')',
        '-.--.-': "'",
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
    }[morse]


def decode_morse(morse_code):

    morse_code = morse_code.lstrip().rstrip()

    if DEBUG >= ON:
        print('Decoding {}'.format(morse_code))

    translation = ""

    # process words
    for word in morse_code.split('   '):

        if translation != '':
            translation += ' '

        # process chars
        for char in word.split(' '):

            translation += decode(char)

    return translation


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("Got {}, expected {}".format(got, expected))
        print(got == expected)
        test.expect(False)


test.describe("Simple")
test_and_print('S', 'S')

test.describe("Decodde 'S'")
test_and_print(decode_morse('...'), 'S')

test.describe("decode 'O")
test_and_print(decode_morse('---'), 'O')

test.describe("Example from description")
test_and_print(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

test.describe("decode 'SOS")
test_and_print(decode_morse('...---...'), 'SOS')

test.describe("Leading and trailing spaces")
test_and_print(decode_morse(' . '), 'E')

test.describe("Big brown fox")
test_and_print(decode_morse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-'),
               'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
