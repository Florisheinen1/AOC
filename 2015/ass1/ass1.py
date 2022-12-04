

LEVEL = 0

BASEMENT = None

char_i = 1
with open("input.txt", 'r') as file:
	for row in file:
		for c in row.rstrip():
			if c == "(":
				LEVEL += 1
			else:
				LEVEL -= 1

			if BASEMENT is None and LEVEL < 0:
				BASEMENT = char_i
			char_i += 1

print(LEVEL)
print(BASEMENT)