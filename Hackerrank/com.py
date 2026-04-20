#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

if __name__ == '__main__':
    s = input()
    
    # 1. Count the occurrences of each character
    counts = Counter(s)
    
    # 2. Sort the items:
    #    First key: -x[1] (count descending)
    #    Second key: x[0] (character ascending)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 3. Print the top 3
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
