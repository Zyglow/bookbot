def pText(runes):
    wrds = runes.split()
    return len(wrds)

def cChars(runes):
    charMap = {}
    lChars = runes.lower()
    for char in lChars:
        if char.isalpha():
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
    return charMap

def sortList(charMap):
    # The instructions for this step say "function takes the dictionary
    # of characters and their counts and returns a sorted list of dictionaries.
    # But,considering the example output, I believe they meant a sorted list of tuples.
    sortedList = sorted(charMap.items(), key=lambda x: x[1], reverse=True)
    return sortedList