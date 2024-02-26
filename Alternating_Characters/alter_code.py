def alternatingCharacters(s):
    # Write your code here
    a = len(s)
    b = 0
    for i in range(0,a-1):
        if s[i] == s[i+1]:
            b += 1
    return b