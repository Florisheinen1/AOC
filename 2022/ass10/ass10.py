
CYCLE = 0 # Nth cycle
X = 1

INSTR_CYCLE = 0

wanted = [20, 60, 100, 140, 180, 220]

COMMANDS = [] # None for noop, int vor addx

with open("input.txt", 'r') as file:
    for row in file.readlines():
        if row.rstrip() == "noop":
            COMMANDS.append(None)
        else:
            v = int(row.rstrip().split(" ")[1])
            COMMANDS.append(v)

OTHER_COMMANDS = COMMANDS.copy()

SPRITE_POS = list("###" + "." * 37)

def doCycle():
    global CYCLE, X, COMMANDS, INSTR_CYCLE

    cmd = COMMANDS[0]            

    # First, handle finished command
    if cmd == None:
        if INSTR_CYCLE == 1:
            COMMANDS.pop(0)
            INSTR_CYCLE = 0
    else:
        if INSTR_CYCLE == 2:
            COMMANDS.pop(0)
            INSTR_CYCLE = 0
            X += cmd

    INSTR_CYCLE += 1
    CYCLE += 1
    # print(CYCLE, X, INSTR_CYCLE, cmd)

def printMonitor():
    global FRAME
    # print(FRAME)
    for r in FRAME:
        print("".join(r))

def setSpritePos(pos):
    global SPRITE_POS
    # Clear sprite pos
    SPRITE_POS = list("."*40)

    # Draw sprite pos
    left = pos-1
    right = pos+1

    if left >= 0 and left < len(SPRITE_POS):
        SPRITE_POS[left] = "#"
    if pos >= 0 and pos < len(SPRITE_POS):
        SPRITE_POS[pos] = "#"
    if right >= 0 and right < len(SPRITE_POS):
        SPRITE_POS[right] = "#"

def drawInFrame():
    global X, CYCLE, FRAME, SPRITE_POS
    setSpritePos(X)
    row = CYCLE // 40
    col = (CYCLE-1) % 40

    pixel = SPRITE_POS[col]

    if row < 6:
        FRAME[row][col] = SPRITE_POS[col]

FRAME = [list("."*40), list("."*40), list("."*40), list("."*40), list("."*40), list("."*40)]

SUM = 0
while COMMANDS:
    doCycle()
    if CYCLE in wanted:
        SUM += CYCLE * X
    drawInFrame()
    

print(SUM)

printMonitor()