from repository.validare_date import Validator
def citire_client_nou():
    try:    
        client_id = input("Introduceti ID-ul clientului nou. (Numarul natural): > ")
        Validator.validare_id(client_id)
        print("ID client este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None
    
    try:
        nume = input("Introduceti numele si prenumele clientului: > ")
        Validator.validare_nume(nume)
        print("Numele clientului este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None
    
    try:    
        CNP = input("Introduceti CNP-ul clientului. (SAAMMZZJJZZZC): > ")
        Validator.validare_CNP(CNP)
        print("CNP este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None
    return client_id, nume, CNP
    
def citire_carte_noua():
    try:
        book_id = input("Introduceti ID-ul cartii noi. (Numarul natural): > ")
        Validator.validare_id(book_id)
        print("ID cartii este valid.")
    except ValueError as ex:
        print("Excepție neașteptată:", ex)
        return None, None, None, None
        
    titlu = input("Intoduceti titlul cartii: > ")
    try:    
        descriere = input("Introduceti descrierea cartii: > ")
        Validator.validare_descriere(descriere)
        print("Descrierea cartii este valida.")
    except ValueError as ex:
        print("Excepție neașteptată:", ex)
        return None, None, None, None
    try:
        autor = input("Introduceti autorul cartii: > ")
        Validator.validare_nume(autor)
        print("Numele autorului este valid")
    except ValueError as ex:
        print("Excepție neașteptată:", ex)
        return None, None, None, None
    return book_id, titlu, descriere, autor

def citire_imprumut_nou():
    try:
        client_id = input("Introduceti ID-ul clientului care realizeaza imprumurtul. (Numarul natural): > ")
        Validator.validare_id(client_id)
        print("ID client este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None, None, None
    
    try:
        book_id = input("Introduceti ID-ul cartii ce se va imprumuta. (Numarul natural): > ")
        Validator.validare_id(book_id)
        print("ID carte este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None, None, None
    
    try:
        data_inceput = input("Introduceti data la care se realizeaza imprumutul. (ZZ.LL.AAAA): > ")
        Validator.validare_zi(data_inceput)
        print("Ziua este valida.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None, None, None
    
    try:    
        data_final = input("Introduceti data la care se va returna imprumutul. (ZZ.LL.AAAA): > ")
        Validator.validare_zi(data_final)
        print("Ziua este valida.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None, None, None
    
    try:
        status = input("Citeste statusul imprumului. (Returnat/Nereturnat/Restant): > ")
        Validator.validare_status(status)
        print("Statusul este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None, None, None, None, None
    
    return client_id, book_id, data_inceput, data_final, status

def citire_clientID():
    try:
        client_id = input("Introduceti ID-ul clientului (Numarul natural): > ")
        Validator.validare_id(client_id)
        print("ID client este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return client_id
    
def citire_clientNUME():
    try:
        nume = input("Introduceti numele si prenumele clientului: > ")
        Validator.validare_nume(nume)
        print("Numele clientului este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return nume
    
def citire_clientCNP():
    try:    
        CNP = input("Introduceti CNP-ul clientului. (SAAMMZZJJZZZC): > ")
        Validator.validare_CNP(CNP)
        print("CNP este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return CNP
           
def citire_bookID():
    try:
        book_id = input("Introduceti ID-ul cartii (Numarul natural): > ")
        Validator.validare_id(book_id)
        print("ID client este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return book_id
    
def citire_bookTITLU():
    titlu = input("Intoduceti titlul cartii: > ")
    return titlu

def citire_bookDESCRIERE():
    try:    
        descriere = input("Introduceti descrierea cartii: > ")
        Validator.validare_descriere(descriere)
        print("Descrierea cartii este valida.")
    except ValueError as ex:
        print("Excepție neașteptată:", ex)
        return None
    return descriere

def citire_bookAUTOR():
    try:
        autor = input("Introduceti autorul cartii: > ")
        Validator.validare_nume(autor)
        print("Numele autorului este valid")
    except ValueError as ex:
        print("Excepție neașteptată:", ex)
        return None
    return autor

def citire_imprumutDATA_INCEPUT():
    try:
        data_inceput = input("Introduceti data la care se realizeaza imprumutul. (ZZ.LL.AAAA): > ")
        Validator.validare_zi(data_inceput)
        print("Ziua este valida.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return data_inceput
    
def citire_imprumutDATA_FINAL():
    try:
        data_final = input("Introduceti data la care se va returna imprumutul. (ZZ.LL.AAAA): > ")
        Validator.validare_zi(data_final)
        print("Ziua este valida.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return data_final
    
def citire_imprumutSTATUS():
    try:
        status = input("Citeste statusul imprumului. (Returnat/Nereturnat/Restant): > ")
        Validator.validare_status(status)
        print("Statusul este valid.")
    except ValueError as ex:
        print("Exceptie neasteptata:", ex)
        return None
    return status
    
    
    
    

    

