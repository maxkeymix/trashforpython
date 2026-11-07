filein = open("input.txt")
fileout = open("output.txt", "w")

d = dict()
d1 = dict()

for i in filein:
    for j in i.split():
            d[j] = d.get(j, 0) + 1

for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    d1[k] = v


for k, v in d1.items():
    fileout.write(f"{k}")
    break

filein.close()
fileout.close()