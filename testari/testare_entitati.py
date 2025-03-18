from domain.carte import Carte
from domain.client import Client
from domain.imprumut import Imprumuturi

"""
    Teste CLIENT
"""


def test_get_client_id():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    assert client_test1.get_client_id() == "1"
    client_test2 = Client("2", "Popovici Marius", "5020202331332")
    assert client_test2.get_client_id() == "2"
    

def test_get_client_nume():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    assert client_test1.get_client_nume() == "Popescu Ion"
    client_test2 = Client("2", "Popovici Marius", "5020202331332")
    assert client_test2.get_client_nume() == "Popovici Marius"
    

def test_get_client_CNP():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    assert client_test1.get_client_CNP() == "5010408330531"
    client_test2 = Client("2", "Popovici Marius", "5020202331332")
    assert client_test2.get_client_CNP() == "5020202331332"
 

def test_set_client_id():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    client_test1.set_client_id("2")
    assert client_test1.get_client_id() == "2"
    client_test2 = Client("3", "Popovici Marius", "5020202331332")
    client_test2.set_client_id("1")
    assert client_test2.get_client_id() == "1"
    

def test_set_client_nume():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    client_test1.set_client_nume("Badea Daniel")
    assert client_test1.get_client_nume() == "Badea Daniel"
    client_test2 = Client("2", "Popovici Marius", "5020202331332")
    client_test2.set_client_nume("Ionescu Matei")
    assert client_test2.get_client_nume() == "Ionescu Matei"
    

def test_set_client_CNP():
    client_test1 = Client("1", "Popescu Ion", "5010408330531")
    client_test1.set_client_CNP("5020202331332")
    assert client_test1.get_client_CNP() == "5020202331332"
    client_test2 = Client("2", "Popovici Marius", "5020202331332")
    client_test2.set_client_CNP("5010408330531")
    assert client_test2.get_client_CNP() == "5010408330531"
    

test_get_client_id()
test_get_client_nume()
test_get_client_CNP()
test_set_client_id()
test_set_client_nume()
test_set_client_CNP()

"""
    Teste CARTE
"""


def test_get_book_id():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    assert carte_test_1.get_book_id() == "1000"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    assert carte_test_2.get_book_id() == "1001"
    
def test_set_book_id():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    carte_test_1.set_book_id("1002")
    assert carte_test_1.get_book_id() == "1002"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    carte_test_2.set_book_id("1003")
    assert carte_test_2.get_book_id() == "1003"
    
def test_get_titlu():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    assert carte_test_1.get_titlu() == "Amintiri din copilarie"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    assert carte_test_2.get_titlu() == "Ion"
    
def test_set_titlu():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    carte_test_1.set_titlu("Amintiri")
    assert carte_test_1.get_titlu() == "Amintiri"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    carte_test_2.set_titlu("Iona")
    assert carte_test_2.get_titlu() == "Iona"
    
def test_get_descriere():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    assert carte_test_1.get_descriere() == "scolara"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    assert carte_test_2.get_descriere() == "roman"
    
def test_set_descriere():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    carte_test_1.set_descriere("poveste")
    assert carte_test_1.get_descriere() == "poveste"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    carte_test_2.set_descriere("nuvela")
    assert carte_test_2.get_descriere() == "nuvela"
    
def test_get_autor():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    assert carte_test_1.get_autor() == "Ion Creanga"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    assert carte_test_2.get_autor() == "Ioan Slavici"
    
def test_set_autor():
    carte_test_1 = Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga")
    carte_test_1.set_autor("Mihai Eminescu")
    assert carte_test_1.get_autor() == "Mihai Eminescu"
    carte_test_2 = Carte("1001", "Ion", "roman", "Ioan Slavici")
    carte_test_2.set_autor("Mircea Cartarescu")
    assert carte_test_2.get_autor() == "Mircea Cartarescu"
    
test_get_book_id()
test_set_book_id()
test_get_titlu()
test_set_titlu()
test_get_descriere()
test_set_descriere()
test_get_autor()
test_set_autor()

"""
    Teste IMPRUMUTURI
"""

def test_get_imprumut_client():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    assert imprumut_test_1.get_imprumut_client() == "1"
    imprumut_test_2 = Imprumuturi("2", "1001", "01.02.2021", "10.02.2023", "Nereturnat")
    assert imprumut_test_2.get_imprumut_client() == "2"
    
def test_set_imprumut_client():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    imprumut_test_1.set_imprumut_client("3")
    assert imprumut_test_1.get_imprumut_client() == "3"
    imprumut_test_2 = Imprumuturi("3", "1001", "01.02.2023", "10.02.2023", "Incheiat")
    imprumut_test_2.set_imprumut_client("4")
    assert imprumut_test_2.get_imprumut_client() == "4"

def test_set_status():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Nereturnat")
    imprumut_test_1.set_status("Returnat")
    assert imprumut_test_1.get_status() == "Returnat"
    imprumut_test_2 = Imprumuturi("2", "1001", "01.02.2021", "10.02.2023", "Restant")
    imprumut_test_2.set_status("Restant")
    assert imprumut_test_2.get_status() == "Restant"
    
def test_get_data_inceput():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    assert imprumut_test_1.get_data_inceput() == "01.01.2023"
    imprumut_test_2 = Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")
    assert imprumut_test_2.get_data_inceput() == "15.03.2022"

def test_get_data_final():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    assert imprumut_test_1.get_data_final() == "10.01.2023"
    imprumut_test_2 = Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")
    assert imprumut_test_2.get_data_final() == "25.03.2022"

def test_get_status():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    assert imprumut_test_1.get_status() == "Returnat"
    imprumut_test_2 = Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")
    assert imprumut_test_2.get_status() == "Nereturnat"

def test_set_data_inceput():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Nereturnat")
    imprumut_test_1.set_data_inceput("31.12.2022") 
    assert imprumut_test_1.get_data_inceput() == "31.12.2022"

def test_set_data_final():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Nereturnat")
    imprumut_test_1.set_data_final("28.02.2023")
    assert imprumut_test_1.get_data_final() == "28.02.2023"
    
def test_get_imprumut_book():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    assert imprumut_test_1.get_imprumut_book() == "1000"
    imprumut_test_2 = Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")
    assert imprumut_test_2.get_imprumut_book() == "1001"

def test_set_imprumut_book():
    imprumut_test_1 = Imprumuturi("1", "1000", "01.01.2023", "10.01.2023", "Returnat")
    imprumut_test_1.set_imprumut_book("2000")
    assert imprumut_test_1.get_imprumut_book() == "2000"
    imprumut_test_2 = Imprumuturi("2", "1001", "15.03.2022", "25.03.2022", "Nereturnat")
    imprumut_test_2.set_imprumut_book("3001")
    assert imprumut_test_2.get_imprumut_book() == "3001"
    
test_get_imprumut_client()
test_set_imprumut_client()
test_get_imprumut_book()
test_set_imprumut_book()
test_get_data_inceput()
test_set_data_inceput()
test_get_data_final()
test_set_data_final()
test_get_status()
test_set_status()
