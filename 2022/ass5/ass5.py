# First in list is on top of stack

def get_crates_from_row(row):
	crates = []
	for i in range(1, len(row), 4):
		crates.append(row[i])
	return crates

def is_initial_crates_row(row):
	return "[" in row

def get_initial_stacks_from_input(rows):
	stacks = {}
	for row in rows:
		if not is_initial_crates_row(row):
			break

		row_crates = get_crates_from_row(row)
		
		stack_num = 1
		for c in row_crates:
			if not c == " ":
				if stack_num not in stacks:
					stacks[stack_num] = []

				stacks[stack_num].append(c)

			stack_num += 1
	return stacks

def get_stacks():
	with open("input.txt", 'r') as file:
		stacks_unsorted = get_initial_stacks_from_input(file.readlines())
		stacks = dict(sorted(stacks_unsorted.items()))
		return stacks

STACKS = get_stacks()

def move_crate(from_stack, to_stack):
	to_stack = from_stack[:1] + to_stack
	from_stack = from_stack[1:]

def move_crates(amount, from_stack, to_stack):
	for i in range(amount):
		move_crate(from_stack, to_stack)

def getTopStacks(stacks):
	tops = []
	for key in stacks:
		tops.append(stacks[key][0])
	return tops

def is_row_operation(row):
	return "move" in row

# returns amount, from stack, to stack
def get_things_of_operation(row):
	spl = row.split(" ")
	amount = int(spl[1])
	from_stack = int(spl[3])
	to_stack = int(spl[5])
	return (amount, from_stack, to_stack)

def get_operations():
	ops = []
	with open("input.txt", 'r') as file:
		for row in file.readlines():
			if is_row_operation(row):
				ops.append(get_things_of_operation(row))
	return ops

def do_operation(stacks, op):
	for i in range(op[0]):
		stacks[op[2]] = stacks[op[1]][:1] + stacks[op[2]]
		stacks[op[1]] = stacks[op[1]][1:]

def do_operation2(stacks, op):
	length = op[0]
	fro = op[1]
	to = op[2]
	stacks[op[2]] = stacks[op[1]][:op[0]] + stacks[op[2]]
	stacks[op[1]] = stacks[op[1]][op[0]:]

def do_operations_1():
	stacks = get_stacks()
	for op in get_operations():
		do_operation(stacks, op)
	return "".join(getTopStacks(stacks))

print(do_operations_1())

def do_operations_2():
	stacks = get_stacks()
	for op in get_operations():
		do_operation2(stacks, op)
	return "".join(getTopStacks(stacks))

print(do_operations_2())