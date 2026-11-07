filein = open("input.txt")
fileout = open("output.txt", "w")

d = dict()

for i in filein:
    for j in i.split():
        print(d.get(j, 0), file=fileout)
        d[j] = d.get(j, 0) + 1
fileout.close()
filein.close()