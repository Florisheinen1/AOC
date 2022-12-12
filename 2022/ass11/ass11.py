MONKEYS = {} # id to monkey object

class Monkeee:
	def __init__(self, number):
		self.number = number
		self.items = None
		self.operation = None
		self.testDivBy = None
		self.passTo = None
		self.failTo = None
		self.inspected = 0
		self.willRelieve = True
		
	def doTurn(self):
		self.inspectItems()
		if self.willRelieve:
			self.relieve()
		else:
			self.noRelieve()
		self.throwItems()

	def inspectItems(self):
		for i in range(len(self.items)):
			self.items[i] = self.operation(self.items[i])
			self.inspected += 1

	def relieve(self):
		for i in range(len(self.items)):
			self.items[i] = int(self.items[i] / 3)

	def noRelieve(self):
		global NO_RELIEVE
		for i in range(len(self.items)):
			self.items[i] = int(self.items[i] % NO_RELIEVE)

	def throwItems(self):
		global MONKEYS

		throwables = [x for x in self.items if x % self.testDivBy == 0]
		keep = [x for x in self.items if not x % self.testDivBy == 0]

		for item in throwables:
			MONKEYS[self.passTo].items.append(item)

		for item in keep:
			MONKEYS[self.failTo].items.append(item)

		self.items.clear()

	def __str__(self):
		return "Monkey " + str(self.number) + ": " + str(self.items)

def parseOperation(result_string):
	first, op, second = result_string.split(" ")

	fL = (lambda x : x) if first == "old" else (lambda x: int(first))
	sL = (lambda x : x) if second == "old" else (lambda x: int(second))
	
	if op == "+":
		return lambda x : fL(x) + sL(x)
	elif op == "-":
		return lambda x : fL(x) - sL(x)
	elif op == "*":
		return lambda x : fL(x) * sL(x)

def getMonkeyFromInput():
	monkeees = {}

	currentMonkey = None
	with open("input.txt", 'r') as file:
		for row in file.readlines():
			if "Monkey" in row:
				number = int(row.rstrip().split(" ")[1][:-1])
				
				currentMonkey = Monkeee(number)
				monkeees[number] = currentMonkey
			elif "Starting" in row:
				numbers_string = row.rstrip().split(":")[1]
				split = numbers_string.split(",")

				numbers = []
				for s in split:
					numbers.append(int(s[1:]))

				currentMonkey.items = numbers

			elif "Operation" in row:
				result_string = row.rstrip().split("=")[1].strip()
				op = parseOperation(result_string)
				currentMonkey.operation = op
			
			elif "Test" in row:
				currentMonkey.testDivBy = int(row.split(" ")[-1])
			elif "true" in row:
				currentMonkey.passTo = int(row.rstrip().split(" ")[-1])
			elif "false" in row:
				currentMonkey.failTo = int(row.rstrip().split(" ")[-1])
	return monkeees

MONKEYS = getMonkeyFromInput()

def doRound():
	global MONKEYS
	for monk in MONKEYS.values():
		monk.doTurn()

def getMonkeyBusiness():
	global MONKEYS
	l = list(MONKEYS.values())
	l.sort(reverse=True, key=lambda x : x.inspected)
	return l[0].inspected * l[1].inspected

for i in range(20):
	doRound()

print(getMonkeyBusiness())

######################

MONKEYS = getMonkeyFromInput()
for m in MONKEYS.values():
	m.willRelieve = False

MUL = 1
testDivisors = []
for m in MONKEYS.values():
	testDivisors.append(m.testDivBy)
	MUL = MUL * m.testDivBy

NO_RELIEVE = MUL

for i in range(10000):
	doRound()
print(getMonkeyBusiness())
