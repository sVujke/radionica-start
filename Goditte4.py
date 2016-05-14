plejliste = {
        'rok': ['Resistance', 'Gasoline', "It's so easy"],
        'pop': ['Hello', 'Happy'],
        'rep': ['Rap God', 'What happened', 'California Love']
    }


for plejlista in plejliste:
    
    lista_pesama = plejliste[plejlista]

    print "Ova plejlista ima: %d pesame " % len(lista_pesama)
    print "Ime ove plejliste je: "+ plejlista+"\n"
    print "Plejlistu cine: "
    for pesma in plejliste[plejlista]:
        print pesma