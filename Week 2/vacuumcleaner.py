import random
rooms = [random.choice([0, 1]), random.choice([0, 1])]
curr = 0

def check(ind):
    if not ind:
        return "Clean"
    return "Dirty"

while(1):
    print(rooms)
    print(f"Location: Room{curr + 1}, Status: {check(rooms[curr])}")
    if rooms[curr] == 1:
        rooms[curr] = 0
        print(f"Room{curr + 1} cleaned")
        curr = (curr + 1) % 2
        if rooms[curr] == 0:
            rooms[curr] = random.choice([0, 1])
            if rooms[curr]:
                print(f"Room{curr + 1} got dirty!")
        if rooms[curr] == 0:
            break
    else:
        curr = (curr + 1) % 2
        if rooms[curr] == 0:
            break
print(rooms)
print("All rooms are clean")
