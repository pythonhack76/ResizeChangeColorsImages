#gestione dizionario e trasformazione


dizionario_test = {'a': 'Utenti', 'b': 'clienti', 'c': 'sponsors', 'd': 'managers'}

listOfKeys = dizionario_test.keys() 
print('tipi di variabile listOfKeys : ', type(listOfKeys))

listOfKeys = list(listOfKeys)

print("stampo tutte le occorrenze e tutte le chiavi:")
print(listOfKeys)

print("stampo le chiavi individuali nella lista:")

for key in listOfKeys:
    print(key)

listofValues = dizionario_test.values()

listOfValues = list(listofValues)


for val in listOfValues:
    print(val[:1])