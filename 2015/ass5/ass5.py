
wrong = ["ab", "cd", "pq", "xy"]

vowels = "aeiou"

def contains_double(s):
	for i in range(len(s) - 1):
		current = s[i]
		nex = s[i+1]
		if current == nex:
			return True
	return False

def contains_wrong(s):
	global wrong
	for w in wrong:
		if w in s:
			return True
	return False

def count_vowels(s):
	i = 0
	for c in s:
		if c in vowels:
			i += 1
	return i


def is_nice(s):
	return count_vowels(s) >= 3 and not contains_wrong(s) and contains_double(s)

NICE = 0

with open("input.txt", 'r') as file:
	for row in file:
		if is_nice(row.rstrip()):
			NICE += 1

print(NICE)


def has_duplicate_pairs(s):
	for i in range(len(s) - 1):
		current_pair = s[i:i+2]
		if current_pair in s[i+2:]:
			return True
	return False

def has_repeats(s):
	for i in range(len(s)-2):
		if s[i] == s[i+2]:
			return True
	return False

def is_nice_2(s):
	return has_repeats(s) and has_duplicate_pairs(s)

NICE = 0

with open("input.txt", 'r') as file:
	for row in file:
		if is_nice_2(row.rstrip()):
			NICE += 1

print(NICE)

