if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract all scores and find the unique second minimum
    scores = sorted({s[1] for s in students})
    second_lowest_score = scores[1]
    
    # Filter students with that score and sort their names alphabetically
    result = sorted([s[0] for s in students if s[1] == second_lowest_score])
    
    # Print each name on a new line
    for name in result:
        print(name)
