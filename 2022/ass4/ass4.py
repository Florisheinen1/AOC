

def get_range(a, b):
	l = []
	i = a
	while i <= b:
		l.append(i)
		i+=1
	return l
	
def is_range_contained(a, b):
	for x in a:
		if x not in b:
			return False
	return True

def fully_overlap(a, b):
	return is_range_contained(a, b) or is_range_contained(b, a)

def parse(row):
	a = row.split("-")
	b = a[1].split(",")
	return int(a[0]), int(b[0]), int(b[1]), int(a[2])

def somewhat_overlaps(a, b):
	for c in a:
		if c in b:
			return True
	for c in b:
		if c in a:
			return True
	return False

COUNTER = 0

with open("input.txt", 'r') as file:
	for row in file:
		a, b, c, d = parse(row.rstrip())

		first = get_range(a, b)
		second = get_range(c, d)
		if fully_overlap(first, second):
			COUNTER += 1

print(COUNTER)


#####################

COUNTER = 0

with open("input.txt", 'r') as file:
	for row in file:
		a, b, c, d = parse(row.rstrip())

		first = get_range(a, b)
		second = get_range(c, d)
		if somewhat_overlaps(first, second):
			COUNTER += 1

print(COUNTER)