n = int(input())
events = input()
rooms = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for event in events:
    if event == 'L':
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break  
    elif event == 'R':
        for i in range(9, -1, -1):
            if rooms[i] == 0:
                rooms[i] = 1
                break  
    else:
        room_number = int(event)
        rooms[room_number] = 0
for room in rooms:
    print(room, end="")
print()