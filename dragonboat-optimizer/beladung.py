def optimale_beladung(insassen):
    insassen = sorted(insassen, key=lambda x: x['gewicht'], reverse=True)
    gruppen = {'vorne': [], 'mitte': [], 'hinten': []}

    for insasse in insassen:
        gruppe = insasse['gruppe']
        gruppen[gruppe].append(insasse)

    links = []
    rechts = []

    for gruppe in gruppen.values():
        gruppe = sorted(gruppe, key=lambda x: x['gewicht'])
        anzahl = len(gruppe)
        for i, insasse in enumerate(gruppe):
            if i < anzahl // 2:
                links.append(insasse)
            else:
                rechts.append(insasse)

    beladung = {'links': links, 'rechts': rechts}
    return beladung
