
import re

regex = re.compile(r'(\d+)-(\d+) (.): ([a-z]+)')

f = open('day02a_password_philosophy_input.txt', 'r')
values = []
nvalid = 0
for l in f.readlines():
    m = regex.search(l)
    if not m:
        continue
    low, high, character, password = m.group(1), m.group(2), m.group(3), m.group(4)
    low, high = int(low), int(high)
    values.append((low, high, character, password))
    #print((low, high, character, password))
    count = 0
    for c in password:
        if c == character:
            count += 1
            if count > high:
                break
    if low <= count and count <= high:
        nvalid += 1

print(nvalid)
