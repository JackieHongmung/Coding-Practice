def romanToInt(s):
    romanDict = {"I": 1,
        "V": 5,
        "X": 10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    value = 0
    prevNum = 0
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