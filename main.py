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
#La seguente divide meglio le keyword trovate ed elimina i punti ed altri elementi presenti nella splitlist
def dividi_contenuto(source,splitlist):
 i=0
 list=[]
 posini=0
 pos = 0

 for e in source:
    for y in splitlist:
        if e==y:
     
       
            pos=i
            if source[posini:pos] in splitlist:
                posini = i+1
            else:    
                print "Elemento char"+e
                print "posini"+str(posini)
                print "pos"+str(pos)
                print "i"+str(i)
                list.append(source[posini:pos])
                posini = i+1
    print "posini totale:" + str(posini)
    print "pos totale:" +str(pos)
    print "i totali"+str(i)    
    print "totale lunghezza stringa:"+str(len(source))
    if pos <> len(source)-1:
        if i == len(source)-1:
            list.append(source[posini:i+1])
    i=i+1
 return list




# pagina, l'ho definita url....nel secondo campo di input della procedura seguente
# Nella seguente procedura il contenuto trovato viene suddiviso in parole. Per ogni parola
# si chiama la procedura aggiungi_indice che aggiunge o meno la parola e l'url all'indice
def aggiungi_pagina_indice (indice,url,contenuto):
       #Utilizzo una procedura per dividere il contenuto a seconda di alcuni caratteri indicati in una stringa. Questo per determinare delle parole (keyword) migliori
  
       parole = dividi_contenuto(contenuto,'.,-+ <>/\;"=():[]%$&?^{}!|#_')
       #parole = contenuto.split()
       print parole
       for parola in parole:
                aggiungi_indice(indice,parola,url)

#indice e' composto da un vettore che nel primo elemento(entry), 
#contiene il valore keyword e nel secondo una lista con gli url ad esso connessi
#La seguente procedura se trova una keyword gia' contenuta nell'indice aggiunge url, altrimenti sia la keywork che l'url
def aggiungi_indice(indice,keyword,url):
        for entry in indice:  
            if entry[0] == keyword:
              if url not in entry[1]: #elimina gli url duplicati per la stessa keyword
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
#Nella seguente aggiungete il primo link (http....) o seme (xxxxxxxxxxxxx) da cui partire
#con yyyyyy si intende la parola (o keyword) da ricercare tra gli url associati
#Non funziona ancora correttamente sulle pagine con frame
risultato = crawler_engine_uno("xxxxxxxxxxxxxxxx")
print ricerca(risultato,'yyyyyyyyyyyyyyy')



