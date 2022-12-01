
calories = [0]

with open("input.txt", 'r') as file:



	for line in file:
		data = line.rstrip()
		if data == "":
			calories.append(0)
		else:
			current = int(data)
			calories[len(calories)-1] += current

print(max(calories))

max1 = max(calories)
calories.remove(max1)
max2 = max(calories)
calories.remove(max2)
max3 = max(calories)

print(max1 + max2 + max3)
