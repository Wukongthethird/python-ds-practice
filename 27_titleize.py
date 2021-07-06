def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    w_phrase_list = []
    w_phrase = phrase.split(' ')
    for word in w_phrase:
        w_phrase_list.append(word.capitalize()) 

    return ' '.join(w_phrase_list)


