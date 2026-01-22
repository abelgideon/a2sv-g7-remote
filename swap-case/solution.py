def swap_case(s):
    finalString = []
    for ch in s:
        if ch >= "a" and ch <= "z":
            finalString.append(ch.upper())
        elif ch >= "A" and ch <= "Z":
            finalString.append(ch.lower())
        else:
            finalString.append(ch)
        
    return "".join(finalString)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)