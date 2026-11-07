filein = open("input.txt")
fileout = open("output.txt", "w")

r = dict()
d = {
    "read": "R",
    "write": "W",
    "execute": "X"
}
arer = 0 
arew = 0


for i in filein:
    if not(arer) and i.strip("\n").isdigit():
        arer = 1
        arew = 0
    elif arer and i.strip("\n").isdigit():
        arew = 1
        arer = 0
    if arer:
        if not(i.strip("\n").isdigit()) and i.strip():
            n, cd = i.split(maxsplit= 1) # name, can do
            r[n] = cd
    if arew:
        if not(i.strip("\n").isdigit()) and i.strip():
            ac, n = i.split()
            if d.get(ac, 0) in r.get(n, -1):
                print("OK", file= fileout)
            else:
                print("Access denied", file= fileout)


filein.close()
fileout.close()