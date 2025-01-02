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
    if len(argv) != 2:
        pError("the arguments are bad.")
    
    try:
        s = str(argv[0]).split()
        nbr = int(argv[1])
        cmp = lambda x: True if len(x) > nbr else False
        list = [item for item in s if cmp(item)]
        print(list)
    except:
        pError("the arguments are bad.")


if __name__ == '__main__':
    main(sys.argv[1:])