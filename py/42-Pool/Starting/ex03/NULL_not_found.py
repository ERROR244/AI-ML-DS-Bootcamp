def NULL_not_found(object: any) -> int:
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False

    if object is Nothing:
        print(f'Nothing: ', end='')
    elif object != object:
        print(f'Cheese: ', end='')
    elif type(object) == int and object == Zero:
        print(f'Zero: ', end='')
    elif object is Empty:
        print(f'Empty: ', end='')
    elif type(object) == bool and object == Fake:
        print(f'Fake: ', end='')
    else:
        print('Type not Found')
        return 1
    print(f'{object} {type(object)}')
    return 0