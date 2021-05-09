
f = open('day01a_report_repair_input.txt', 'r')
values = []
for l in f.readlines():
    val_str = l.strip()
    if len(val_str) > 0:
        val = int(val_str)
        values.append(val)

values = sorted(values)
#for v in values:
#    print(v)

i, j = 0, len(values)-1


for i in range(len(values)):
    a = values[i]
    if a > 2020:
        break
    for j in range(i+1, len(values)):
        b = values[j]
        if a+b > 2020:
            break
        for k in range(j+1, len(values)):
            c = values[k]
            if a + b + c == 2020:
                print(a, b, c, a*b*c)
