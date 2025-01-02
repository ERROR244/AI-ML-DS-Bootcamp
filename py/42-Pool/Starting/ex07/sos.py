import sys

def pError(error):
    """
    print an error.
    Args:
        error (str): The error to print.
    Returns:
        none.
    """

    print(f"AssertionError: {error}")
    exit()

def main(argv):
    if len(argv) != 1:
        pError("the arguments are bad.")
    
    try:
        NESTED_MORSE = {'A':'.-',      'B':'-...',
                        'C':'-.-.',    'D':'-..',
                        'E':'.',       'F':'..-.',
                        'G':'--.',     'H':'....',
                        'I':'..',      'J':'.---',
                        'K':'-.-',     'L':'.-..',
                        'M':'--',      'N':'-.',
                        'O':'---',     'P':'.--.',
                        'Q':'--.-',    'R':'.-.',
                        'S':'...',     'T':'-',
                        'U':'..-',     'V':'...-',
                        'W':'.--',     'X':'-..-',
                        'Y':'-.--',    'Z':'--..',
                        '1':'.----',   '2':'..---',
                        '3':'...--',   '4':'....-',
                        '5':'.....',   '6':'-....',
                        '7':'--...',   '8':'---..',
                        '9':'----.',   '0':'-----',
                        ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..',  '/':'-..-.',
                        '-':'-....-',  '(':'-.--.',
                        ')':'-.--.-'}
        s = str(argv[0])
        res = ''
        if type(s) != str or sum(1 for c in s if c in set("!\"#%&'()*+,-./:$;<=>?@[]^_`{|}~")) != 0:
            raise ValueError("the arguments are bad.")
        for letter in s:
            if (letter != ' '):
                print(NESTED_MORSE[letter.upper()] + ' ', end='')
            else:
                print(end=' ')
        print()
    except ValueError as e:
        pError(e)


if __name__ == '__main__':
    main(sys.argv[1:])
