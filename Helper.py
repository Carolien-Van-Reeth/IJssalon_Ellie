def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(dictionary):
    totaal = 0
    for waarde in dictionary.values():
        totaal += waarde
    return totaal
