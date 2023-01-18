#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    var = 0
    s = roman_string
    if (isinstance(s, str) is not True or s is None):
        return(0)
    for i in range(len(s)):
        if i+1 < len(s) and val[s[i]] < val[s[i+1]]:
            var -= val[s[i]]
        else:
            var += val[s[i]]
    return (var)
