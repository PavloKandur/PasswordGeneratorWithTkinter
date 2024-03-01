from random import choice

def password_without_spec(length:int)->str:
    """
    Name: password_without_spec
    input parameters: length
    type length: int
    function return str object
    """
    password = ""
    alphabeth_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabeth_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = list(range(11))
    list_items = [alphabeth_low, alphabeth_cap, numbers]
    for _ in range(length):
        tmp = choice(list_items)
        password += str(choice(tmp))
    return password

def password_with_spec(length:int)->str:
    """
    Name: password_with_spec
    input parameters: length
    type length: int
    function return str object
    """
    password = ""
    alphabeth_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabeth_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = list(range(11))
    spec_items=['!', '#', '$', '%', '&', '*', '+', '-', '.', '/', '<', '=', '>', '?', '@', '^', '_', '|', '~']
    list_items = [alphabeth_low, alphabeth_cap, numbers,spec_items]
    for _ in range(length):
        tmp = choice(list_items)
        password += str(choice(tmp))
    return password

