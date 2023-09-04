def any_lowercase1(s):
    """
    This function terminate after the first letter is checked
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """
    It will always return the String 'True', because the loop is terminated after the first iteration.
    In each iteration, the string 'c' is checked if it is lower case, which is always true.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """
    This function checks only the last character in the string if it is lower case or not.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """
    This function does the actual checks and return the correct value, because it keeps track, if there is
    a lower case char in the string.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """
    This function terminates after the first encounter of an uppercase character and then returns false.
    It will only return True, if the string contains only lowercase characters.
    """
    for c in s:
        if not c.islower():
            return False
    return True


def call_function(fun, words):
    print("")
    for w, value in words.items():
        print(f"{fun.__name__}({w}) => {fun(w)} <=> {value}")


if __name__ == "__main__":
    words = {"Hello": True, "hEELO": True, "HeLlO": True, "hello": True, "HELLO": False}
    call_function(any_lowercase1, words)
    call_function(any_lowercase2, words)
    call_function(any_lowercase3, words)
    call_function(any_lowercase4, words)
    call_function(any_lowercase5, words)
