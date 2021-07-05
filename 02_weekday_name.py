def weekday_name(day_of_week):

    if day_of_week not in range(1,8):
        return None
    
    weekdays = ["Sunday" , "Monday" , "Tuesday" , "Wenesday", "Thursday" , "Friday" , " Saturday"]

    return weekdays[day_of_week-1]

    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

print( weekday_name(9) )

