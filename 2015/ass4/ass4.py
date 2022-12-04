inp = "yzbqklnj"

import hashlib

def enc(a):
	return hashlib.md5(a.encode('utf-8')).hexdigest()

# letters = range(ord("a"), ord("z") + 1)
# nums = range(ord("0"), ord("9") + 1)

# def chars(a, b):
# 	yield from a
# 	yield from b

def find(inp):
	i = 0
	while True:
		i+= 1
		hs = inp + str(i)
		en = enc(hs)
		first = en[:5]
		try:
			if int(first) == 0:
				return i
		except:
			continue

print(find("yzbqklnj"))

def find2(inp):
	i = 0
	while True:
		i+= 1
		hs = inp + str(i)
		en = enc(hs)
		first = en[:6]
		try:
			if int(first) == 0 and en[6] != "0":
				return i
		except:
			continue

print(find2("yzbqklnj"))