def dodaj_plejlistu(plejlista, lista_pesama):
        plejliste[plejlista] = lista_pesama
        #print plejliste

print "Hocete li da unesete novu plejlistu (da/ne): \n"
da_ne = raw_input()

vrti = False

def da_li_vrti(tekst):
    if da_ne == "da":
        vrti = True
    else:
        vrti = False 
    return vrti

plejliste = {}
vrti = da_li_vrti(da_ne)

#print vrti 
while vrti:
    print "Unesi naziv plejliste: \n"
    ime_plejliste = raw_input()
    print "Unesi nazive pesama i razdvoji ih @ simbolom: \n"
    pesme = raw_input()

    
    pesme = pesme.split('@')

    dodaj_plejlistu(ime_plejliste, pesme)
    
    print "Hocete li da unesete novu plejlistu (da/ne): \n"
    da_ne = raw_input()
    vrti = da_li_vrti(da_ne)
    
print plejliste

