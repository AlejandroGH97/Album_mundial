with open("nombres_figuritas.txt") as i:
    faltan_nom = i.readlines()
faltan_nom = [x.strip("\n")  for x in faltan_nom]

for m in faltan_nom:
    if m[0] == " ":
        m = m.strip(str(" "))

with open("nombres_figuritas.txt", "w") as l:
    for entry in faltan_nom:
        l.write(entry+'\n')
