from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    choice = int(input("1 - Peržiūrėti\n2 - Įvesti pajamas\n3 - Įvesti išlaidas\n4 - Balansas\n0 - Išeiti\n"))
    match choice:
        case 1:
            print(biudzetas.zurnalas)
        case 2:
            biudzetas.prideti_pajamas()
        case 3:
            biudzetas.prideti_islaidas()
        case 4:
            print("Balansas", biudzetas.gauti_balansa())
        case 0:
            break
