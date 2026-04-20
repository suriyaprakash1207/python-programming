# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import OrderedDict

def solve():
    # Read all input lines and strip whitespace
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:]
    
    word_counts = OrderedDict()
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # Output number of distinct words
    print(len(word_counts))
    
    # Output the counts in order of first appearance
    print(*(word_counts.values()))

if __name__ == "__main__":
    solve()
