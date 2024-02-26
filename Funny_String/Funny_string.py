def funnyString(s):
    a = s[::-1]
    b = len(s)
    first = []
    secord = [] 
    for i in range(0,b-1):
        one = abs(ord(s[i])-ord(s[i+1]))
        two = abs(ord(a[i])-ord(a[i+1]))
        first.append(one)
        secord.append(two)
        
    if first == secord:
        return 'Funny'
    else:
        return 'Not Funny'
    
    
