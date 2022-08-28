def replace_space(string: str) -> str:
    """Replace space in a string with '%20'.

    :param str string: a string
    :raises ValueError: String is empty
    :return str: returned string
    """
    if len(string) == 0:
        raise ValueError("String is empty.")

    length_space = 0
    for s in string:
        if s == " ":
            length_space += 1

    length_new = len(string) + length_space * 2
    new_string = [" "] * length_new
    index_original = len(string) - 1
    index_new = length_new - 1
    while index_new >= index_original and index_original >= 0:
        if string[index_original] == " ":
            new_string[index_new - 2 : index_new + 1] = ["%", "2", "0"]
            index_new -= 3
            index_original -= 1
        else:
            new_string[index_new] = string[index_original]
            index_original -= 1
            index_new -= 1
    return "".join(new_string)
