
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

while True:
    sm = values[i] + values[j]
    if i > j:
        break
    elif sm == 2020:
        print(i, j, values[i] * values[j])
        j -= 1
        i += 1
    elif sm > 2020:
        j -= 1
    else:
        i += 1
