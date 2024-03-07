import math
import os
import random
import re
import sys


def alternate(s):
    # Write your code here
    text= list(set(s))
    
    result = ''
    
    for i in range(len(text) - 1):
        for j in range(i + 1, len(text)):
            text2= f'[^{text[i]}{text[j]}]'
            str_replaced = re.sub(text2, '', s)
            if not re.search(r'(.)\1', str_replaced) and len(str_replaced) > len(result):
                result = str_replaced
    
    return len(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
