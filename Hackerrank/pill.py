# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    t = int(input_data[0])
    current_line = 1
    
    for _ in range(t):
        n = int(input_data[current_line])
        blocks = list(map(int, input_data[current_line + 1].split()))
        current_line += 2
        
        left = 0
        right = n - 1
        last_picked = float('inf')
        possible = True
        
        while left <= right:
            # Pick the larger of the two ends
            if blocks[left] >= blocks[right]:
                picked = blocks[left]
                left += 1
            else:
                picked = blocks[right]
                right -= 1
            
            # Check if it violates the stacking rule
            if picked > last_picked:
                possible = False
                break
            
            last_picked = picked
            
        print("Yes" if possible else "No")

if __name__ == "__main__":
    solve()
