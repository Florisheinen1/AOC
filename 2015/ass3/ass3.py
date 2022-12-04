def up(a):
	return a[0], a[1] + 1
def down(a):
	return a[0], a[1] -1
def left(a):
	return a[0] - 1, a[1]
def right(a):
	return a[0] + 1, a[1]

CURRENT = (0, 0)
PACKETS = {CURRENT: 1}

with open("input.txt", 'r') as file:
	for row in file:
		for c in row.rstrip():
			if c == "^":
				CURRENT = up(CURRENT)
			elif c == "v":
				CURRENT = down(CURRENT)
			elif c == ">":
				CURRENT = right(CURRENT)
			elif c == "<":
				CURRENT = left(CURRENT)
			else:
				print("Ah oh", c)
			if CURRENT not in PACKETS:
				PACKETS[CURRENT] = 0
			PACKETS[CURRENT] += 1

print(len(PACKETS))

#################################
def split_parts(s):
	a = []
	b = []
	i = 0
	for c in s:
		if i % 2 == 0:
			a.append(c)
		else:
			b.append(c)
		i+= 1
	return a, b

CURRENT_SANTA = (0, 0)
CURRENT_ROBOT = (0, 0)
PACKETS = {CURRENT_SANTA: 1}

with open("input.txt", 'r') as file:
	a, b = split_parts(file.read().rstrip())


	for c in a:
		if c == "^":
			CURRENT_SANTA = up(CURRENT_SANTA)
		elif c == "v":
			CURRENT_SANTA = down(CURRENT_SANTA)
		elif c == ">":
			CURRENT_SANTA = right(CURRENT_SANTA)
		elif c == "<":
			CURRENT_SANTA = left(CURRENT_SANTA)
		else:
			print("Ah oh", c)
		if CURRENT_SANTA not in PACKETS:
			PACKETS[CURRENT_SANTA] = 0
		PACKETS[CURRENT_SANTA] += 1

	for c in b:
		if c == "^":
			CURRENT_ROBOT = up(CURRENT_ROBOT)
		elif c == "v":
			CURRENT_ROBOT = down(CURRENT_ROBOT)
		elif c == ">":
			CURRENT_ROBOT = right(CURRENT_ROBOT)
		elif c == "<":
			CURRENT_ROBOT = left(CURRENT_ROBOT)
		else:
			print("Ah oh", c)
		if CURRENT_ROBOT not in PACKETS:
			PACKETS[CURRENT_ROBOT] = 0
		PACKETS[CURRENT_ROBOT] += 1


print(len(PACKETS))