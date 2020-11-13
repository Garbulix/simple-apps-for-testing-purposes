

def reversed(some_string):
    reversed_string = ''
    last_letter_index = len(some_string) - 1

    for current_index in range(len(some_string)):
        reversed_string = reversed_string + some_string[last_letter_index - current_index]

    return reversed_string

def check_palindrome(some_string):
    if len(some_string) < 2:
        return False
    else:
        return some_string.upper() == reversed(some_string.upper())   # should be case insensitive