def caesarCipher(s, k):
    answer = ''
    for i in s:
        if 'a' <= i <= 'z':
            answer += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= i <= 'Z':
            answer += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
        else:
            answer += i
    return answer