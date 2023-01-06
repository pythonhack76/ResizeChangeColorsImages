class Test:
    def addNumeri(x,y):
        return x + y

Test.addNumeri = staticmethod(Test.addNumeri)

print('Prodotto:', Test.addNumeri(20, 20))


class Calcolatore:

    @staticmethod
    def aggiungiNumeri(x, y):
        return x + y

print('Prodotto:', Calcolatore.aggiungiNumeri(30, 100))

#funzione esempio json load
def importaDati():

    import json 
    #apro il file 
    f = open('data.json')

    data = json.load(f)

    #itero il json list
    for i in data['emp_details']:
        print(i)

    f.close() 

importaDati() 


def leggiDatiJson(dati="dati di esempio"):
    import json
    f = open('data.json', "r")

    #leggi dal file
    data = json.loads(f.read())

    #itera attraverso la lista json
    for i in data['emp_details']:
        print(i)
        elenco_json = json.dumps(data)

        elenco_ = elenco_json.encode("utf-8")
        print(elenco_)
        how_many_data = len(elenco_)
    if(len(elenco_)  > 3):
        print(dati)
        print(how_many_data)
     

    f.close() 

leggiDatiJson() 


def mostraEccezioni():
    while True:
        try:
            x = int(input("inserisci un numero:"))
            break
        except ValueError:
            print("occhio! non è valido. Riprova!")


if __name__ == '__leggiDatiJson__':
    mostraEccezioni() 
else:
    print("non posso procedere")


class Utenti:
    """ classe di test per Utenti """
    messaggio: str = f'abbiamo testato correttamente il file'
    def __init__(self):
        return self.messaggio
      

user = Utenti() 