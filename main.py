def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"


def getprossimolink(pagina):
    posiniziale = pagina.find('<a href=')
    if posiniziale==-1:
            return None,0
    inizioquote = pagina.find('"',posiniziale)
    finequote = pagina.find('"',inizioquote+1)
    url = pagina[inizioquote+1:finequote]
    return url,finequote            

def stampatuttiilinks(pagina):
    while True:
        url,posfinale = getprossimolink(pagina)
        if url:
            print url
            pagina = pagina[posfinale:]
        else:
            break



stampatuttiilinks(get_page('https://it.wikipedia.org/wiki/Linux'))
