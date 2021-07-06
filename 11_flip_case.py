def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_string = ""

# can use .swapcase for strings
    for letter in phrase:
        if letter == to_swap.upper():
            new_string += letter.lower()
        elif letter == to_swap.lower():
            new_string += letter.upper()
        else:
            new_string += letter
    
    return new_string
