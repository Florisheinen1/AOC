import numpy as np

def dist(a, b):
    return abs(b - a)

def getTargetPos(a, dir):
    if dir == "L":
        return a + (-1, 0)
    elif dir == "R":
        return a + (1, 0)
    elif dir == "U":
        return a + (0, 1)
    elif dir == "D":
        return a + (0, -1)

def getNewPos(head, dir, tail):
    nextHead = getTargetPos(head, dir)
    d = dist(nextHead, tail)
    if sum(d) == 3:
        nextTail = head
        return nextHead, nextTail

    if sum(d) == 2 and max(d) > 1:
        nextTail = head
        return nextHead, nextTail
    
    return nextHead, tail

visited = [] # List of tuples of coords

TAIL = np.array([0, 0])
HEAD = np.array([0, 0])

def executeCommand(dir, count):
    global HEAD, TAIL

    for i in range(count):
        HEAD, TAIL = getNewPos(HEAD, dir, TAIL)
        if not tuple(TAIL) in visited:
            visited.append(tuple(TAIL))

with open("input.txt", 'r') as file:
    for row in file.readlines():
        split = row.rstrip().split(" ")
        direction = split[0]
        count = int(split[1])
        executeCommand(direction, count)

print(len(visited))

#######################################

LEN = 10

def getNextPosOfTail(newHead, currentTail):
    distance = newHead - currentTail
    if max(abs(distance)) >= 2:
        # This means head is out of range of tail
        s = sum(abs(distance))
        if s == 2:
            # The head moved in a straight line from the tail
            return currentTail + np.int_(distance / 2)
        elif s == 3 or s == 4:
            # The head moved (somewhat) diagonally from the tail
            return currentTail + np.int_(distance / abs(distance))
        else:
            print("Ah oh!")
    return currentTail

def getNextRope(dir, knots):
    newRope = [getTargetPos(knots[0], dir)]
    for tailPiece in knots[1:]:
        newTailPiece = getNextPosOfTail(newRope[-1], tailPiece)
        newRope.append(newTailPiece)
    return newRope

def executeCommand2(dir, count):
    global ROPE, visited2
    for i in range(count):
        ROPE = getNextRope(dir, ROPE)
        tailPos = tuple(ROPE[-1])
        if tailPos not in visited2:
            visited2.append(tailPos)

ROPE = [np.array([0, 0])] * 10
visited2 = []

with open("input.txt", 'r') as file:
    for row in file.readlines():
        split = row.rstrip().split(" ")
        direction = split[0]
        count = int(split[1])
        executeCommand2(direction, count)
print(len(visited2))