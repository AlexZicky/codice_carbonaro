print('***********************************************')
print('*      DECOFIFICATORE DI CODICE CARBONARO     *')
print('*             BY ALEXZICKY (c)2024            *')
print('***********************************************\n')

def codice_carbonaro():
    alfabeto_chiaro  = 'aàbcdeèflms' +'oòpgtiìvrnz'
    alfabeto_cifrato = 'oòpgtiìvrnz' +'aàbcdeèflms'
    decodifica = ''
    print('Insersci testo da decodificare: \n')
    codice = input()

    for c in codice:
        ciclo = 0
        # print(c)
        for l in alfabeto_chiaro:
            if c in alfabeto_chiaro or c in alfabeto_chiaro.upper():
                if  c == l or c== l.upper():
                    if c.isupper():
                        decodifica = decodifica + alfabeto_cifrato[ciclo].upper()
                        break   
                    else:
                        decodifica = decodifica + alfabeto_cifrato[ciclo]
                        break   
                else:
                    ciclo += 1
            else:
                decodifica = decodifica + c
                break

    print('\n'+decodifica+'\n')

def ripeti():
    while True:
        scelta = input("Premi 'q' per uscire dal programma o 'r' per codificare/decodifiacre un'altro messaggio: ")
        
        if scelta == 'q':
            print("Uscita dal programma.")
            break
        elif scelta == 'r':
            codice_carbonaro()
        else:
            print("Scelta non valida. Riprova.")
            
codice_carbonaro()
ripeti()
