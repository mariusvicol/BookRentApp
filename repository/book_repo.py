from domain.carte import Carte
from repository.validare_date import Validator
from utils.utils import deep_copy_lista
from exception.exception import BookAlreadyExistsException
import unittest

class CarteInMemoryRepo:
    def __init__(self):
        self.__carti = []
        
    def get_carti(self):
        return self.__carti
    
    def set_lista_carti(self, carti_noi):
        self.__carti = deep_copy_lista(carti_noi)
        
    def set_carti(self, carte_noua):
        self.__carti.append(carte_noua)  
        
    def adaugare_carte_noua(self, book_id, titlu, descriere, autor):
        """
            Adauga o carte noua in biblioteca
            ;param book_id: ID cartii
            ;type book_id: string de cifre
            ;param titlu: Titlul cartii
            ;type titlu: string
            ;param descriere: Descrierea cartii
            ;type descriere: string
            ;param autor: Autorul cartii
            ;type autor: string
        """
        try:
            Validator.validare_id(book_id)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_descriere(descriere)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_nume(autor)
        except ValueError as ex:
            raise ex
        
        for carte in self.__carti:
            if carte.get_book_id() == book_id:
                raise BookAlreadyExistsException()
    
        carte_noua = Carte(book_id, titlu, descriere, autor)
        self.set_carti(carte_noua) 
        
    def sterge_bookID(self, book_id):
        """
            Sterge cartile cu id-ul dat
            ;param book_id: ID cartii
            ;type book_id: string de cifre
        """
        carti_nesterse = []
        for carte in self.__carti:
            if carte.get_book_id() != book_id:
                carti_nesterse.append(carte)
        self.set_lista_carti(carti_nesterse)
        
    def cautare_carteID(self, bookID):
        """
            Cauta o carte dupa ID-ul citit si returneaza celelalte date ale cartii
            ;param bookID: ID-ul cartii
            ;type bookID: string
            ;retrun: titlu, descriere, autor
            ;rtype: string, string, string
        """
        for carte in self.get_carti():
            if bookID == carte.get_book_id():
                return carte.get_titlu(), carte.get_descriere(), carte.get_autor()

class CarteFileRepo(CarteInMemoryRepo):
    def __init__(self, filename):
        """
            Constructorul clasei
        """
        CarteInMemoryRepo.__init__(self)
        self.__filename = filename
        self.__incarcare_carte_din_fisier()
        
    def __incarcare_carte_din_fisier(self):
        """
            Incarca cartile din fisier
        """
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line == "\n":
                    break
                bookID, titlu, descriere, autor = [token.strip() for token in line.split(";")]

                CarteInMemoryRepo.adaugare_carte_noua(self, bookID, titlu, descriere, autor)

                
    def incarca_carte_in_fisier(self):
        """
            Incarca cartile in fisier
        """
        with open(self.__filename, "w") as f:
            carti = CarteInMemoryRepo.get_carti(self)
            for carte in carti:
                carte_str = carte.get_book_id() + " ; " + carte.get_titlu() + " ; " + carte.get_descriere() + " ; " + carte.get_autor() + "\n"
                f.write(carte_str)
                
    def get_carti(self):
        """
           Suprascrie get carti din repo
        """
        return CarteInMemoryRepo.get_carti(self)
        
    def set_carti(self, carte_noua):
        """
            Suprascrie set carti din repo
        """
        CarteInMemoryRepo.set_carti(self, carte_noua)
        self.incarca_carte_in_fisier()
        
    def set_lista_carti(self, carti_noi):
        """
            Suprascrie set lista carti din repo
        """
        CarteInMemoryRepo.set_lista_carti(self, carti_noi)
        self.incarca_carte_in_fisier()
        
    def sterge_bookID(self, bookID):
        """
            Suprascrie sterge_bookID din repo
        """
        CarteInMemoryRepo.sterge_bookID(self, bookID)
        self.incarca_carte_in_fisier()
        
    def cautare_carteID(self, bookID):
        """
            Suprascrie cautare_carteID din repo
        """
        return CarteInMemoryRepo.cautare_carteID(self, bookID)
        
    def adaugare_carte_noua(self, book_id, titlu, descriere, autor):
        CarteInMemoryRepo.adaugare_carte_noua(self, book_id, titlu, descriere, autor)
        self.incarca_carte_in_fisier()

# class TestCarteFileRepo(unittest.TestCase):
#     def setUp(self):
#         self.filename = "test_carti.txt"
#         with open(self.filename, "w") as f:
#             carte_sir = "1 ; Ion ; roman ; Liviu Rebreanu"
#             f.write(carte_sir)
#         self.repo = CarteFileRepo(self.filename)
#
#     def tearDown(self):
#         with open("test_carti.txt", "w"):
#             pass
#
#     def test_incarcare_carte_din_fisier(self):
#         carti = self.repo.get_carti()
#         self.assertEqual(len(carti), 1)
#         self.assertEqual(carti[0].get_titlu(), "Ion")
#
#     def test_incarca_carte_in_fisier(self):
#         carte_noua = Carte("2", "Mara", "nuvela", "Marin Preda")
#         self.repo.set_carti(carte_noua)
#         carti = self.repo.get_carti()
#         self.assertEqual(len(carti), 2)
#         self.assertEqual(carti[1].get_titlu(), "Mara")