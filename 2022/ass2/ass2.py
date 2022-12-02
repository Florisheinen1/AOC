
def convert(t):
	if t == "A" or t == "X":
		return "ROCK"
	if t == "B" or t == "Y":
		return "PAPER"
	if t == "C" or t == "Z":
		return "SCISSOR"
	print("OI!: ", t)

def score_type(t):
	if t == "ROCK":
		return 1
	if t == "PAPER":
		return 2
	if t == "SCISSOR":
		return 3
	print("OI: ", t)

def score_win(op, me):
	if op == "ROCK" and me == "PAPER" or op == "PAPER" and me == "SCISSOR" or op == "SCISSOR" and me == "ROCK":
		return 6
	if op == me:
		return 3
	return 0

def get_necessary(opp, me):
	if me == "PAPER":
		return opp
	if me == "ROCK":
		if opp == "ROCK":
			return "SCISSOR"
		if opp == "PAPER":
			return "ROCK"
		if opp == "SCISSOR":
			return "PAPER"
	if me == "SCISSOR":
		if opp == "ROCK":
			return "PAPER"
		if opp == "PAPER":
			return "SCISSOR"
		if opp == "SCISSOR":
			return "ROCK"

def score(opponent, me):
	return score_type(me) + score_win(opponent, me)

SCORE = 0

with open("input.txt", 'r') as file:
	for row in file:
		opp = convert(row[0])
		me = convert(row[2])

		actual_me = get_necessary(opp, me)

		SCORE += score(opp, actual_me)

print(SCORE)