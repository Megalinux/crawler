#programma crawler per la cattura dei links. Si tratta di una prima versione di test.
#procedura get_page per l'apertura della pagina web
def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

#procedura per la ricerca dei links tramite la string a <a href
def getprossimolink(pagina):
    posiniziale = pagina.find('<a href=')
    if posiniziale==-1:
            return None,0
    inizioquote = pagina.find('"',posiniziale)
    finequote = pagina.find('"',inizioquote+1)
    url = pagina[inizioquote+1:finequote]
    return url,finequote            

#nella lista links registro tutti i link trovati nella pagina
def get_tutti_i_links(pagina):
    links = []
    while True:
        url,fineposizionelink = getprossimolink(pagina)
        if url:
            links.append(url)
            pagina = pagina[fineposizionelink:]
        else:
            break
    return links

# scorro gli elementi della lista dei links trovati e se questi non sono presenti nella prima lista (li aggiungo all'ultimo)
def unione(p,q):
    for e in q:
        if e not in p:
            p.append(e)


# pagina, l'ho definita url....nel secondo campo di input della procedura seguente
# Nella seguente procedura il contenuto trovato viene suddiviso in parole. Per ogni parola
# si chiama la procedura aggiungi_indice che aggiunge o meno la parola e l'url all'indice
def aggiungi_pagina_indice (indice,url,contenuto):
       parole = contenuto.split()
       for parola in parole:
                aggiungi_indice(indice,parola,url)

#indice e' composto da un vettore che nel primo elemento(entry), 
#contiene il valore keyword e nel secondo una lista con gli url ad esso connessi
#La seguente procedura se trova una keyword gia' contenuta nell'indice aggiunge url, altrimenti sia la keywork che l'url
def aggiungi_indice(indice,keyword,url):
        for entry in indice:  
            if entry[0] == keyword:
                entry[1].append(url)

        indice.append([keyword,[url]])



#Nella seguente procedura si cerca nell'indice la keyword e si ritornano gli url ad essa associati.
#se non vi sono non ritorna nulla
def ricerca(indice,keyword):
          for entry in indice:
               if entry[0] == keyword:
                   return entry[1]

          return[]                                        


#registro nella lista nonvisitati il seed (il sito origine). Nella lista visitati vi sono i
#links gia visitati.

def crawler_engine_uno(seed):
    nonvisitati = [seed]
    visitati = []
    indice = [] #aggiungi un indice dove eseguire le ricerce
    while nonvisitati:
        pagina = nonvisitati.pop()
        if pagina not in visitati:
            print"************************************"
            print get_tutti_i_links(get_page(pagina))
            print "link non visitati prima di unione"
            print nonvisitati
            contenuto = get_page(pagina)
            aggiungi_pagina_indice(indice,pagina,contenuto)
            unione(nonvisitati,get_tutti_i_links(get_page(pagina)))
            print "link non visitati dopo unione"
            print nonvisitati
        
            visitati.append(pagina)
            print "---------------------------------------"
            print "visitati dopo aggiunta pagina visitata" 
            print visitati
            print"************************************"



    return indice

#Devo trovare un link che non sia troppo pieno di links!!!    
#Nella seguente aggiungete il primo link (http....) o seme da cui partire
print crawler_engine_uno('xxxxxxxxxxxxxxxxx')


