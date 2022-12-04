
def charToNum(c):
	o = ord(c) - 96
	if o < 0:
		o += 31 + 27
	return o

def split_in_two(s):
	if len(s) % 2 != 0:
		print("Odd number: ", s)
	a = s[0:int(len(s)/2)]
	b = s[int(len(s)/2):]
	return a, b

def duplicates(a, b):
	dupl = []
	for x in a:
		for y in b:
			if x == y:
				if x not in dupl:
					dupl.append(x)
	return dupl

def handle_backpack(back):
	a, b = split_in_two(back)
	ds = duplicates(a, b)[0]
	return charToNum(ds)

SUM = 0

with open("input.txt", 'r') as file:
	for row in file:
		a = handle_backpack(row.rstrip())
		SUM += a

print(SUM)

#########################

def handle_backpack_2(a, b, c):
	dupl_ab = duplicates(a,b)
	dupl_bc = duplicates(b, c)
	dupl = duplicates(dupl_ab, dupl_bc)
	if len(dupl) != 1:
		print("Ehhh", dupl)
	return charToNum(dupl[0])

SUM = 0
i = 0
with open("input.txt", 'r') as file:

	lines = file.readlines()

	for i in range(int(len(lines) / 3)):
		first = lines[i * 3].rstrip()
		second = lines[i * 3 + 1].rstrip()
		third = lines[i * 3 + 2].rstrip()

		a = handle_backpack_2(first, second, third)
		SUM += a
		i += 1

print(SUM)