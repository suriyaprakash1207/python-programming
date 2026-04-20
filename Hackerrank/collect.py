# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys

def solve():
    # Read all input lines
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    d = deque()
    
    # Process each command
    for i in range(1, n + 1):
        parts = input_data[i].split()
        method_name = parts[0]
        
        # Check if the method requires an argument (like append 1)
        if len(parts) > 1:
            val = parts[1]
            getattr(d, method_name)(val)
        else:
            getattr(d, method_name)()
            
    # Print the space-separated elements
    print(*(d))

if __name__ == "__main__":
    solve()
