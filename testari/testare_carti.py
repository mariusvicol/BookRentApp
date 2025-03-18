from domain.carte import Carte
from repository.book_repo import CarteInMemoryRepo
from service.carte_service import CarteService
from exception.exception import BookAlreadyExistsException


def test_set_lista_carti():
    carti = CarteInMemoryRepo()
    carti_noi = [Carte("1000", "Amintiri din copilarie", "scolara", "Ion Creanga"), Carte("1001", "Ion", "roman", "Ioan Slavici")]
    carti.set_lista_carti(carti_noi)
    assert carti.get_carti() == carti_noi
    
def test_set_carti():
    carti = CarteInMemoryRepo()
    carte_noua = Carte("1000", "Amintiri din copilărie", "Scolară", "Ion Creangă")
    carti.set_carti(carte_noua)
    assert carti.get_carti() == [carte_noua]
    
def test_adaugare_carte_noua():
    carti = CarteInMemoryRepo()
    carti.adaugare_carte_noua("1", "Ion", "Romanul Ion scris de Liviu Rebreanu", "Liviu Rebreanu")
    assert len(carti.get_carti()) == 1

    try:
        carti.adaugare_carte_noua("1", "Enigma Otiliei", "Romanul Enigma Otiliei scris de George Călinescu", "George Călinescu")
    except BookAlreadyExistsException as e:
        assert str(e) == "Repository Exception: Cartea exista deja."

    carti.adaugare_carte_noua("2", "Morometii", "Romanul Morometii scris de Marin Preda", "Marin Preda")
    assert len(carti.get_carti()) == 2

def test_sterge_bookID():
    carti = CarteInMemoryRepo()
    carte1 = Carte("1000", "Amintiri din copilărie", "Scolară", "Ion Creangă")
    carte2 = Carte("1001", "Ion", "Roman", "Liviu Rebreanu")
    carti.set_lista_carti([carte1, carte2])
    carti.sterge_bookID("1000")
    assert carti.get_carti() == [carte2]
    
def test_sterge_bookTITLU():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])

    carti.sterge_bookTITLU("Mândrie și prejudecată")

    assert carti_repo.get_carti() == [carte2]

def test_sterge_bookDESCRIERE():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])

    carti.sterge_bookDESCRIERE("O carte despre dragoste")

    assert carti_repo.get_carti() == [carte2]

def test_sterge_bookAUTOR():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])

    carti.sterge_bookAUTOR("Jane Austen")

    assert carti_repo.get_carti() == [carte2]
    
def test_modificare_bookTITLU():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carti.modificare_bookTITLU(carte1, "Amintiri din copilarie")
    
    carti_list = carti_repo.get_carti()
    assert carti_list[0].get_titlu() == "Amintiri din copilarie"
    
def test_modificare_bookDESCRIERE():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carti.modificare_bookDESCRIERE(carte1, "O carte despre iubire")
    
    carti_list = carti_repo.get_carti()
    assert carti_list[0].get_descriere() == "O carte despre iubire"
    
def test_modificare_bookAUTOR():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carti.modificare_bookAUTOR(carte1, "Lev Tolstoi")
    
    carti_list = carti_repo.get_carti()
    assert carti_list[0].get_autor() == "Lev Tolstoi"
    
def test_cautare_carteID():
    carti_repo = CarteInMemoryRepo()
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    titlu, descriere, autor = carti_repo.cautare_carteID("1")
    
    assert titlu == "Mândrie și prejudecată"
    assert descriere == "O carte despre dragoste"
    assert autor == "Jane Austen"
    
def test_cautare_carteTITLU():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carte_list = carti.cautare_carteTITLU("Mândrie și prejudecată")
    for carte in carte_list:
        assert carte == carte1
    
def test_cautare_carteDESCRIERE():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carte_list = carti.cautare_carteDESCRIERE("O carte despre dragoste")
    for carte in carte_list:
        assert carte == carte1
    
def test_cautare_carteAUTOR():
    carti_repo = CarteInMemoryRepo()
    carti = CarteService(carti_repo)
    carte1 = Carte("1", "Mândrie și prejudecată", "O carte despre dragoste", "Jane Austen")
    carte2 = Carte("2", "Crimă și pedeapsă", "Un roman clasic despre crima", "Fiodor Dostoievski")
    carti_repo.set_lista_carti([carte1, carte2])
    
    carte_list = carti.cautare_carteAUTOR("Jane Austen")
    for carte in carte_list:
        assert carte == carte1
    
test_set_lista_carti()
test_set_carti()
test_adaugare_carte_noua()
test_sterge_bookAUTOR()
test_sterge_bookDESCRIERE()
test_sterge_bookID()
test_sterge_bookTITLU()
test_modificare_bookTITLU()
test_modificare_bookDESCRIERE()
test_modificare_bookAUTOR()
test_cautare_carteID()
test_cautare_carteTITLU()
test_cautare_carteDESCRIERE()
test_cautare_carteAUTOR()
