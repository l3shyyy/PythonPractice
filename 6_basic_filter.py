# This program will remove vowels from a phrase. In this case - it is prevent trolls from commenting! 

def disemvowel(string_):
    disallowed = "aeiouAEIOU"
    for i in disallowed:
        string_ = string_.replace(i, "")
    return string_

print(disemvowel("This website is for losers LOL!"))
