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

#registro nella lista nonvisitati il seed (il sito origine). Nella lista visitati vi sono i
#links gia visitati
def crawler_engine_uno(seed):
    nonvisitati = [seed]
    visitati = []
    while nonvisitati:
        pagina = nonvisitati.pop()
        if pagina not in visitati:
            print"************************************"
            print get_tutti_i_links(get_page(pagina))
            print "link non visitati prima di unione"
            print nonvisitati
          
            unione(nonvisitati,get_tutti_i_links(get_page(pagina)))
            print "link non visitati dopo unione"
            print nonvisitati
        
            visitati.append(pagina)
            print "---------------------------------------"
            print "visitati dopo aggiunta pagina visitata" 
            print visitati
            print"************************************"



    return visitati

#Devo trovare un link che non sia troppo pieno di links!!!    

print crawler_engine_uno('http://www.megaoverclock.it/')

