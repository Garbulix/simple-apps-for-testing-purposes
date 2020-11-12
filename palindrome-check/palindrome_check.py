def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False

def reversed(some_string):
    reversed_string = ''
    last_letter_index = len(some_string)-1

    for letter_index in range(last_letter_index, -1, -1):
        reversed_string = reversed_string + some_string[letter_index]

    return reversed_string

def check_palindrome(given_string):
    testing_string = given_string

    str_length = len(testing_string)
    halfed_string = None
    middle_letter = None
    middle_letter_index = None
    made_up_palindrome = None

    if (is_even(str_length)):
        halfed_string = testing_string[:int(str_length / 2)]
        made_up_palindrome = halfed_string + reversed(halfed_string)
    else:
        middle_letter_index = int((str_length - 1) / 2)
        middle_letter = testing_string[middle_letter_index]
        halfed_string = testing_string[:middle_letter_index] # letters before middle letter (except middle letter)
        made_up_palindrome = halfed_string + middle_letter + reversed(halfed_string)

    return made_up_palindrome.upper() == given_string.upper()   # should be case insensitive


print(check_palindrome('Kajak'))