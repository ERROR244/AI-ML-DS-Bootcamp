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

def my_counter(str):
    """
    Count the occurrences of different character types in a string.
    Args:
        str (str): Input string.
    Returns:
        none.
    """

    p = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    print(f'The text contains {len(str)} characters: ')
    print(f'{sum(1 for c in str if c.isupper())} upper letters')
    print(f'{sum(1 for c in str if c.islower())} lower letters')
    print(f'{sum(1 for c in str if c in p)} punctuation marks')
    print(f'{sum(1 for c in str if c.isspace())} spaces')
    print(f'{sum(1 for c in str if c.isdigit())} digits')




def main(argv):
    """
    the main function if the building program.
    Args:
        argv (list): a list allows us to retrieve arguments passed to the building script when run from the command line.
    Returns:
        none.
    """

    l = len(argv)
    if l == 0:
        try:
            s = input("What is the text to count?\n") + ' '
        except:
            print("No text to count")
            exit()
        my_counter(s)
    elif l == 1:
        my_counter(argv[0])
    else:
        pError("more than one argument is provided")



if __name__ == "__main__":
    main(sys.argv[1:])