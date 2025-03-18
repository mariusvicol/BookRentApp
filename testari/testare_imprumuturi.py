from domain.carte import Carte
from domain.client import Client
from domain.imprumut import Imprumuturi
from repository.imprumut_repo import ImprumutInMemoryRepo
from repository.client_repo import ClientInMemoryRepo
from repository.book_repo import CarteInMemoryRepo
from service.imprumut_service import ImprumutService

"""
    Teste BIBLIOTECA
"""

def test_set_lista_imprumuturi():
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi_noi = [Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat"), Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")]
    biblioteca_test.set_lista_imprumuturi(imprumuturi_noi)
    assert biblioteca_test.get_imprumuturi() == imprumuturi_noi

def test_set_imprumuturi():
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumut_nou = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    biblioteca_test.set_imprumuturi(imprumut_nou)
    assert biblioteca_test.get_imprumuturi() == [imprumut_nou]
    
def test_sterge_BIBLIOTECA():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    imprumuturi = ImprumutInMemoryRepo()
    biblioteca_test = ImprumutService(imprumuturi, clienti, carti)  
    client1 = Client("1990101010101", "Ana Popescu", "1990101010101")
    carte1 = Carte("1000", "Amintiri din copilărie", "Scolară", "Ion Creangă")
    imprumut1 = Imprumuturi(client1, carte1, "01.01.2023", "10.01.2023", "Returnat")
    clienti.set_lista_clienti([client1])
    carti.set_lista_carti([carte1])
    imprumuturi.set_lista_imprumuturi([imprumut1])
    
    biblioteca_test.sterge_BIBLIOTECA()
    
    assert clienti.get_clienti() == []
    assert carti.get_carti() == []
    assert imprumuturi.get_imprumuturi() == []
    
def test_adaugare_imprumut():
    biblioteca_test = ImprumutInMemoryRepo()
    biblioteca_test.adaugare_imprumut("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    
    assert biblioteca_test.get_imprumuturi()[0].get_status() == "Returnat"
    
def test_sterge_imprumut_DATA_INCEPUT():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1", "1", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("1", "1", "05.02.2023", "20.02.2023", "Returnat")
    biblioteca_test.set_lista_imprumuturi([imprumut1, imprumut2])
    imprumuturi.sterge_imprumut_DATA_INCEPUT("01.01.2023")
    assert biblioteca_test.get_imprumuturi() == [imprumut2]

def test_sterge_imprumut_DATA_FINAL():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1", "1", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("1", "1", "05.02.2023", "20.02.2023", "Returnat")
    biblioteca_test.set_lista_imprumuturi([imprumut1, imprumut2])
    imprumuturi.sterge_imprumut_DATA_FINAL("15.01.2023")
    assert biblioteca_test.get_imprumuturi() == [imprumut2]

def test_sterge_imprumut_client_ID():
    biblioteca_test = ImprumutInMemoryRepo()
    imprumut1 = Imprumuturi("1", "1", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("1", "1", "05.02.2023", "20.02.2023", "Returnat")
    biblioteca_test.set_imprumuturi(imprumut1)
    biblioteca_test.set_imprumuturi(imprumut2)
    biblioteca_test.sterge_imprumut_client_ID("1")
    assert biblioteca_test.get_imprumuturi() == []

def test_sterge_imprumut_book_ID():
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumut1 = Imprumuturi("1" ,"1", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("1", "1", "05.02.2023", "20.02.2023", "Returnat")
    biblioteca_test.set_lista_imprumuturi([imprumut1, imprumut2])
    biblioteca_test.sterge_imprumut_book_ID("1")
    assert biblioteca_test.get_imprumuturi() == []

def test_sterge_imprumut_STATUS():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1", "1", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("1", "1", "05.02.2023", "20.02.2023", "Returnat")
    biblioteca_test.set_lista_imprumuturi([imprumut1, imprumut2])
    imprumuturi.sterge_imprumut_STATUS("Returnat")
    assert biblioteca_test.get_imprumuturi() == []

test_set_lista_imprumuturi()
test_set_imprumuturi()
test_adaugare_imprumut()
test_sterge_imprumut_client_ID()
test_sterge_imprumut_book_ID()
test_sterge_imprumut_DATA_INCEPUT()
test_sterge_imprumut_DATA_FINAL()
test_sterge_imprumut_STATUS()

"""
    Teste INCHIRIERI
"""

def test_seteaza_statusRETURNAT():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Restant")
    biblioteca_test.set_imprumuturi(imprumut1)
    imprumuturi.seteaza_statusRETURNAT("1", "1000")
    assert imprumut1.get_status() == "Returnat"

def test_seteaza_statusNERETURNAT():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1","1000", "01.01.2023", "15.01.2023", "Restant")
    biblioteca_test.set_imprumuturi(imprumut1)
    imprumuturi.seteaza_statusNERETURNAT("1", "1000")
    assert imprumut1.get_status() == "Nereturnat"

def test_seteaza_statusRESTANT():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    biblioteca_test = ImprumutInMemoryRepo() 
    imprumuturi = ImprumutService(biblioteca_test, clienti, carti)
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Nereturnat")
    biblioteca_test.set_imprumuturi(imprumut1)
    imprumuturi.seteaza_statusRESTANT("1", "1000") 
    assert imprumut1.get_status() == "Restant"
    
test_seteaza_statusNERETURNAT()
test_seteaza_statusRESTANT()
test_seteaza_statusRETURNAT()

"""
    Teste RAPOARTE
"""

def test_clienti_cu_carti_inchiriate_ordonati_dupa_nume():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    imprumuturi = ImprumutInMemoryRepo()
    biblioteca_test = ImprumutService(imprumuturi, clienti, carti) 
    client1 = Client("1", "Ion Popescu", "1990101010101")
    client2 = Client("2", "Ana Maria", "1980808080808")
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("2", "1001", "05.02.2023", "20.02.2023", "Returnat")

    clienti.set_lista_clienti([client1, client2])
    imprumuturi.set_lista_imprumuturi([imprumut1, imprumut2])

    rezultat_asteptat = [("Ana Maria", ["1001"]),("Ion Popescu", ["1000"])]
    rezultat_obtinut = biblioteca_test.clienti_cu_carti_inchiriate_ordonati_dupa_nume()
    assert rezultat_obtinut == rezultat_asteptat
    
def test_clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    imprumuturi = ImprumutInMemoryRepo()
    biblioteca_test = ImprumutService(imprumuturi, clienti, carti) 
    client1 = Client("1", "Ion Popescu", "1990101010101")
    client2 = Client("2", "Ana Maria", "1980808080808")
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Returnat")
    imprumut3 = Imprumuturi("1", "1001","01.01.2023", "15.01.2023", "Returnat")
    imprumut2 = Imprumuturi("2", "1001", "05.02.2023", "20.02.2023", "Returnat")

    clienti.set_lista_clienti([client1, client2])
    imprumuturi.set_lista_imprumuturi([imprumut1, imprumut2, imprumut3])

    rezultat_asteptat = [("Ion Popescu", ["1000","1001"]), ("Ana Maria", ["1001"])]
    rezultat_obtinut = biblioteca_test.clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor()
    assert rezultat_obtinut == rezultat_asteptat

def test_cele_mai_inchiriate_carti():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    imprumuturi = ImprumutInMemoryRepo()
    biblioteca_test = ImprumutService(imprumuturi, clienti, carti) 
    client1 = Client("1", "Ion Popescu", "1990101010101")
    client2 = Client("2", "Ana Maria", "1980808080808")
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Returnat")
    imprumut3 = Imprumuturi("1", "1000","03.01.2023", "15.02.2023", "Returnat")
    imprumut2 = Imprumuturi("2", "1001", "05.02.2023", "20.02.2023", "Returnat")
    imprumut4 = Imprumuturi("2", "1000", "05.03.2023", "20.03.2023", "Returnat")

    clienti.set_lista_clienti([client1, client2])
    imprumuturi.set_lista_imprumuturi([imprumut1, imprumut2, imprumut3, imprumut4])

    rezultat_asteptat = [
        {"book_id": "1000", "numar_inchirieri": 3},
        {"book_id": "1001", "numar_inchirieri": 1}
    ]

    rezultat_obtinut = biblioteca_test.carti_inchiriate_ordonate_dupa_numarul_imprumuturilor()
    assert rezultat_obtinut == rezultat_asteptat

def test_primele_10_la_suta_mai_putin_inchiriate():
    clienti = ClientInMemoryRepo()
    carti = CarteInMemoryRepo()
    imprumuturi = ImprumutInMemoryRepo()
    biblioteca_test = ImprumutService(imprumuturi, clienti, carti)
    imprumut1 = Imprumuturi("1", "1000", "01.01.2023", "15.01.2023", "Returnat")
    imprumut3 = Imprumuturi("1", "1015", "03.01.2023", "15.02.2023", "Returnat")
    imprumut2 = Imprumuturi("2", "1001", "05.02.2023", "20.02.2023", "Returnat")
    imprumut4 = Imprumuturi("2", "1014", "05.03.2023", "20.03.2023", "Returnat")

    imprumuturi.set_lista_imprumuturi([imprumut1, imprumut2, imprumut3, imprumut4])
    assert biblioteca_test.primele_10_la_suta_mai_putin_inchiriate() == "Nu exista imprumuturi pentru a determina numarul de carti inchiriate."
    imprumuturi.set_imprumuturi([])
    imprumut5 = Imprumuturi("3", "1003", "01.01.2023", "15.01.2018", "Restant")
    imprumut6 = Imprumuturi("4", "1004", "03.01.2021", "15.02.2018", "Returnat")
    imprumut7 = Imprumuturi("5", "1005", "05.02.2022", "20.02.2021", "Nereturnat")
    imprumut8 = Imprumuturi("7", "1006", "05.03.2023", "20.03.2022", "Returnat")
    imprumut9 = Imprumuturi("10", "1000", "01.01.2020", "15.01.2022", "Returnat")
    imprumut10 = Imprumuturi("2", "1011", "03.01.2019", "15.02.2022", "Restant")
    imprumut11 = Imprumuturi("3", "1012", "05.02.2018", "20.02.2022", "Returnat")
    imprumut12 = Imprumuturi("1", "1013", "05.03.2017", "20.03.2022", "Nereturnat")
    imprumuturi.set_lista_imprumuturi([imprumut1, imprumut2, imprumut3, imprumut4,imprumut5, imprumut6, imprumut7, imprumut8, imprumut9, imprumut10, imprumut11, imprumut12])

    rezultat_asteptat = [("1001", 1)]
    rezultat_obtinut = biblioteca_test.primele_10_la_suta_mai_putin_inchiriate()
    assert rezultat_asteptat == rezultat_obtinut

test_clienti_cu_carti_inchiriate_ordonati_dupa_nume()
test_clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor()
test_cele_mai_inchiriate_carti()
test_primele_10_la_suta_mai_putin_inchiriate()
