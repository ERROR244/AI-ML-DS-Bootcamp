def pError(error):
    """
    print an error.
    Args:
        error (str): The error to print.
    Returns:
        none.
    """

    print(f"AssertionError: {error}")

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float].
    Args:
        height (list):  list of integers or floats represents height.
        weight (list):  list of integers or floats represents weight.
    Returns:
        res (list): returns a list of BMI values.
    """
    res = []

    if len(height) != len(weight):
        pError("Invalid argument.")
    for Hitem,Witem in zip(height, weight):
        if not isinstance(Hitem, (int, float)) or not isinstance(Witem, (int, float)):
            pError("Invalid argument")
            return ([])
        Hitem = Hitem * 39.37
        Witem = Witem * 2.205
        res.append(((Witem * 703) / Hitem) / Hitem)
    return res

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    Args:
        height (list):  list of integers or floats represents height.
        weight (list):  list of integers or floats represents weight.
    Returns:
        res (list): returns a list of booleans (True if above the limit)..
    """
    res = []

    for item in bmi:
        if not isinstance(item, (int, float)):
            pError("Invalid argument")
            return ([])
        res.append(item > limit)

    return res