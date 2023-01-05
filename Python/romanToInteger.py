def romanToInt(s):
    """function converts a given roman numeral as a string into a integer
    by converting each character in the string to its integer counterpart and either
    subtracting or adding to the total depending on if the previous value is greater
    or lower

    Args:
        s (string): input string of roman numerals that is already valid

    Returns:
        integer: converted version of the roman numeral
    """
    romanDict = {"I": 1,
        "V": 5,
        "X": 10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    value = 0 # keeps track of total value
    prevNum = 0 # keeps track of previous value to determine if subtracting or adding
    for i in range(0,len(s)):
        curRom = s[i]
        curNum = romanDict.get(curRom)
        if prevNum >= curNum:
            value += curNum
        if prevNum < curNum:
            value += curNum - 2*prevNum
        prevNum = curNum
    return value

if __name__ == "__main__":
    print(romanToInt("XIV"))