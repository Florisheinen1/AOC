
def area(l, b, w):
	surfaces = [l * b, b * w, l * w]
	smallest = min(surfaces)
	box_surface = sum(surfaces) * 2
	return box_surface + smallest

TOTAL = 0

with open("input.txt", 'r') as file:
	for row in file:
		dims = row.rstrip().split("x")
		TOTAL += area(int(dims[0]), int(dims[1]), int(dims[2]))

print(TOTAL)

RIBBON = 0
#################
def length(l, b, w):
	lengths = [l, b, w]
	lengths.remove(max(lengths))
	length = sum(lengths) * 2

	ribbon = l * b * w

	return length + ribbon

with open("input.txt", 'r') as file:
	for row in file:
		dims = row.rstrip().split("x")
		RIBBON += length(int(dims[0]), int(dims[1]), int(dims[2]))
	
print(RIBBON)