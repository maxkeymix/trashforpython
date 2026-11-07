filein = open("input.txt")
fileout = open("output.txt", "w")

d = dict()

for i in filein:
    k, v = i.split()
    d[k] = d.get(k, 0) + int(v)

for k, v in sorted(d.items()):
    fileout.write(f"{k} {v}\n")

filein.close()
fileout.close()