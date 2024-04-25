with open("hasla.txt") as plik:

    ileparzystych = 0
    ilenieparzystych = 0

    for linia in plik:
        linia = linia.strip()

        #zad 1
        if(len(linia)%2==0):
            ileparzystych += 1
        else:
            ilenieparzystych += 1

        #zad 2
        if(linia == linia[::-1]):
            print(linia, "\n")

        # zad 3
        for litera in linia:
            if(ord(litera) + ord(litera) == 220):
                print(linia, "\n")

    print("parzyste: ", ileparzystych)
    print("nie parzyste: ", ilenieparzystych)