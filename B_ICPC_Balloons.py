t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    solved_before = set()
    balloons = 0
    
    for letter in s:
        if letter not in solved_before:
            balloons += 2
            solved_before.add(letter)
        else:
            balloons += 1
            
    print(balloons)