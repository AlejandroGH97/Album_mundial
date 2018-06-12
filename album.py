import inspect

with open("nombres_figuritas.txt") as i:
    global nombres_de_figuritas
    nombres_de_figuritas = i.readlines()
nombres_de_figuritas = [x.strip("\n")  for x in nombres_de_figuritas]

with open("paises.txt") as i:
    paises = i.readlines()
paises = [x.strip("\n")  for x in paises]

def menu():
    seguir = raw_input('\n' + "Quieres revisar tu album o tus repetidas? (A/R)\n")
    if seguir.lower() == "a":
        album()
    elif  seguir.lower() == "r":
        funcion_repetidas()
    elif  seguir.lower() == "x" or   seguir.lower() == "exit":
        pass
    else:
        menu()

def pais():
    if figurita.lower() == "logos" or figurita.lower() == "logo":
        lista_equipo = [str(x) for x in range(8,20)]
    if figurita.lower() == "stadiums" or figurita.lower() == "stadium":
        lista_equipo = [str(x) for x in range(8,20)]
    if figurita.lower() == "russia":
        lista_equipo = [str(x) for x in range(20,40)]
    if figurita.lower() == "saudi arabia":
        lista_equipo = [str(x) for x in range(40,60)]
    if figurita.lower() == "egypt":
        lista_equipo = [str(x) for x in range(60,80)]
    if figurita.lower() == "uruguay":
        lista_equipo = [str(x) for x in range(80,100)]
    if figurita.lower() == "portugal":
        lista_equipo = [str(x) for x in range(100,120)]
    if figurita.lower() == "spain":
        lista_equipo = [str(x) for x in range(120,140)]
    if figurita.lower() == "morocco":
        lista_equipo = [str(x) for x in range(140,160)]
    if figurita.lower() == "iran" or figurita.lower() == "ir iran":
        lista_equipo = [str(x) for x in range(160,180)]
    if figurita.lower() == "france":
        lista_equipo = [str(x) for x in range(180,200)]
    if figurita.lower() == "australia":
        lista_equipo = [str(x) for x in range(200,220)]
    if figurita.lower() == "peru":
        lista_equipo = [str(x) for x in range(220,240)]
    if figurita.lower() == "denmark":
        lista_equipo = [str(x) for x in range(240,260)]
    if figurita.lower() == "argentina":
        lista_equipo = [str(x) for x in range(260,280)]
    if figurita.lower() == "iceland":
        lista_equipo = [str(x) for x in range(280,300)]
    if figurita.lower() == "croatia":
        lista_equipo = [str(x) for x in range(300,320)]
    if figurita.lower() == "nigeria":
        lista_equipo = [str(x) for x in range(320,340)]
    if figurita.lower() == "brazil":
        lista_equipo = [str(x) for x in range(340,360)]
    if figurita.lower() == "switzerland":
        lista_equipo = [str(x) for x in range(360,380)]
    if figurita.lower() == "costa rica":
        lista_equipo = [str(x) for x in range(380,400)]
    if figurita.lower() == "serbia":
        lista_equipo = [str(x) for x in range(400,420)]
    if figurita.lower() == "germany":
        lista_equipo = [str(x) for x in range(420,440)]
    if figurita.lower() == "mexico":
        lista_equipo = [str(x) for x in range(440,460)]
    if figurita.lower() == "sweden":
        lista_equipo = [str(x) for x in range(460,480)]
    if figurita.lower() == "korea" or figurita.lower() == "korea republic":
        lista_equipo = [str(x) for x in range(480,500)]
    if figurita.lower() == "belgium":
        lista_equipo = [str(x) for x in range(500,520)]
    if figurita.lower() == "panama":
        lista_equipo = [str(x) for x in range(520,540)]
    if figurita.lower() == "tunisia":
        lista_equipo = [str(x) for x in range(540,560)]
    if figurita.lower() == "england":
        lista_equipo = [str(x) for x in range(560,580)]
    if figurita.lower() == "poland":
        lista_equipo = [str(x) for x in range(580,600)]
    if figurita.lower() == "senegal":
        lista_equipo = [str(x) for x in range(600,620)]
    if figurita.lower() == "colombia":
        lista_equipo = [str(x) for x in range(620,640)]
    if figurita.lower() == "japan":
        lista_equipo = [str(x) for x in range(640,660)]
    if figurita.lower() == "legend" or figurita.lower() == "legends":
        lista_equipo = [str(x) for x in range(660,670)]

    if function_running == "album":
        faltan_equipo = [i for i in lista_equipo if i in faltan_num]
        if len(faltan_equipo) == 0:
            print("\n" + figurita.title() + " esta completo.")

        else:
            for g in lista_equipo:
                if g in faltan_num:
                    print(g + " - " + nombres_de_figuritas[int(g)])

    elif function_running == "funcion_repetidas":
        for g in lista_equipo:
            if g in repetidas:
                print(g + " - " + nombres_de_figuritas[int(g)])


def album():
    global function_running
    function_running = inspect.stack()[0][3]

    with open("faltan_num.txt") as i:
        global faltan_num
        faltan_num = i.readlines()
    faltan_num = [x.strip("\n")  for x in faltan_num]

    global figurita
    figurita = str(raw_input("Que quieres revisar en tu album?\n"))

    if figurita.lower() == "menu" or figurita.lower() == "m":
        menu()
    elif figurita == "?":
        print("Nombre de pais: Cuantas figuritas te faltan del pais.\n#: Cuantas figuritas te faltan.\nNumero de sticker: Revisar si te falta esa figurita.\n")
        album()

    elif figurita == "escudos":
        cromadas_faltan = []
        for x in faltan_num:
            if int(x) % 20 == 0 and int(x) >=20 and int(x) <= 660:
                cromadas_faltan.append(x)
            else:
                pass
        if len(cromadas_faltan) != 0:
            for elementos in cromadas_faltan:
                print(elementos + " - " + nombres_de_figuritas[int(elementos)])
        else:
            print("Ya tienes todos los escudos.")

    elif figurita.isdigit() == True and (int(figurita) > 0 and int(figurita) < 670) or figurita == "0":
        if figurita in faltan_num:

            print(figurita + " - " + nombres_de_figuritas[int(figurita)])
            agregar = str(raw_input("Nola!\nQuieres agregarla al album? (S/N)\n"))

            if agregar.lower() == "s":
                faltan_num.remove(figurita)
                with open("faltan_num.txt", "w") as f:
                    for entry in faltan_num:
                        f.write(entry+'\n')

            elif agregar.lower() == "n":
                pass

        else:
            print(figurita + " - " + nombres_de_figuritas[int(figurita)] + "\nYala.")

    elif figurita.lower() in paises:
        pais()

    elif figurita == "#":
        cromadas_faltan = []
        for x in faltan_num:
            if int(x) % 20 == 0 or int(x) >= 660 or int(x) <=7:
                cromadas_faltan.append(x)
            else:
                pass
        print("\nTe faltan " + str(len(faltan_num)) + " figuritas.\n" + str(len(cromadas_faltan)) + " son cromadas.\n" + str(len(faltan_num)-len(cromadas_faltan)) + " son normales.")

    else:
        print("Ingreso invalido.")
        album()

    album()



def funcion_repetidas():
    global function_running
    function_running = inspect.stack()[0][3]

    with open("repetidas.txt") as r:
        global repetidas
        repetidas = r.readlines()
    repetidas = [x.strip("\n")  for x in repetidas]

    global figurita
    figurita = str(raw_input("Que quieres revisar en tus repetidas?\n"))

    if figurita.lower() == "menu" or figurita.lower() == "m":
        menu()

    elif figurita == "?":
        print("Nombre de pais: Cuantas repetidas tienes del pais.\n#: Cuantas repetidas tienen.\nNumero de sticker: Revisar si teienes esa figurita.\n")
        funcion_repetidas()

    elif figurita.isdigit() == True and (int(figurita) > 0 and int(figurita) < 670) or figurita == "0":
        if figurita in repetidas:

            print(figurita + " - " + nombres_de_figuritas[int(figurita)] + "\nSi la tienes repetida.")
            agregar = str(raw_input("Quieres agregar otra a tu lista, quitar una o hacer nada? (+/-/n)\n"))

            with open("repetidas.txt", "w") as f:
                if agregar == "+":
                    repetidas.append(figurita)
                    for entry in repetidas:
                        f.write(entry+'\n')

                elif agregar.lower() == "-":
                    repetidas.remove(figurita)
                    for entry in repetidas:
                        f.write(entry+'\n')

                elif agregar.lower() == "n":
                    pass
        else:

            print(figurita + " - " + nombres_de_figuritas[int(figurita)] + "\nNo la tienes repetida.")
            agregar = str(raw_input("Quieres agregarla a tu lista de repetidas?(s/n)\n"))

            with open("repetidas.txt", "a") as f:
                if agregar == "s":
                    repetidas.append(figurita)
                    for entry in repetidas:
                        f.write(entry+'\n')

                elif agregar.lower() == "n":
                    pass

    elif figurita == "#":

        cromadas_repetidas = []

        for x in repetidas:
            if int(x) % 20 == 0 and int(x) >=20  or int(x) >= 660 or int(x) <= 7:
                cromadas_repetidas.append(x)
        print("Tienes " + str(len(repetidas)) +" repetidas.\n" + str(len(cromadas_repetidas)) + " son cromadas.\n" + str(len(repetidas)-len(cromadas_repetidas)) + " son normales.")

    elif figurita.lower() in paises:
        pais()

    else:
        print("Ingreso invalido.")
        funcion_repetidas()

    funcion_repetidas()

menu()
