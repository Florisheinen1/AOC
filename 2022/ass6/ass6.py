
def contains_double(l):
    for i in range(len(l)):
        if l[i] in l[i+1:]:
            return True
    return False

def ass(l, count):
    past = []

    for i in range(len(l)):
        c = l[i]
        past.insert(0, c)
        if len(past) > count:
            past.pop()
            if not contains_double(past):
                return i + 1

with open("input.txt", 'r') as file:
    print(ass(file.read(), 4))

# ass 2

with open("input.txt", 'r') as file:
    print(ass(file.read(), 14))
