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

#procedura per la stampa di tutti i links
def stampatuttiilinks(pagina):
    #cicla fino al momento in cui non trovi il valore None (non ci sono più url)
    while True:
        url,posfinale = getprossimolink(pagina)
        if url:
            print "Link trovato:"+url
            pagina = pagina[posfinale:]
        else:
            break



stampatuttiilinks(get_page('https://it.wikipedia.org/wiki/Linux'))
