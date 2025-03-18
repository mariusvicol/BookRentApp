from domain.imprumut import Imprumuturi
from repository.validare_date import Validator
from utils.utils import deep_copy_lista
from exception.exception import RentAlreadyExistsException

class ImprumutInMemoryRepo:
    def __init__(self):
        self.__imprumuturi = []
    
    def get_imprumuturi(self):
        """
            Returneaza lista de imprumuturi
        """
        return self.__imprumuturi

    def recursive_len(self, lst):
        """
        Calculeaza recursiv len lista de imprumuturi
        len(lst)
        """
        if not lst:
            return 0
        else:
            return 1 + self.recursive_len(lst[1:])
        
    def set_lista_imprumuturi(self, imprumuturi_noi):
        """
            Pune o lista noua in locul vechii liste de imprumuturi
        """
        self.__imprumuturi = deep_copy_lista(imprumuturi_noi)               
        
    def set_imprumuturi(self, imprumut_nou):
        """
            Adauga in lista de imprumuturi un imprumut nou
        """
        self.__imprumuturi.append(imprumut_nou)
        
    def exista_imprumut(self, client, carte, data_inceput, data_final, status):
        """
        Verifică dacă există deja un împrumut cu datele specificate în bibliotecă.
        :param client: ID clientului
        :type client: string de cifre
        :param carte: ID cartii
        :type carte: string de cifre
        :param data_inceput: Data la care se face imprumutul
        :type data_inceput: string
        :param data_final: Data la care se va returna imprumutul
        :type data_final: string
        :param status: Statusul imprumutului
        :type status: string
        :return: True dacă există un împrumut cu aceleași date, False altfel
        :rtype: bool
        """
        for imprumut in self.get_imprumuturi():
            if (
                imprumut.get_imprumut_client() == client
                and imprumut.get_imprumut_book() == carte
                and imprumut.get_data_inceput() == data_inceput
                and imprumut.get_data_final() == data_final
                and imprumut.get_status() == status
            ):
                return True
        return False
        
    def adaugare_imprumut(self, client, carte, data_inceput, data_final, status):
        """
            Adauga un imprumut nou in biblioteca
            ;param client: ID clientului
            ;type client: string de cifre
            ;param carte: ID cartii
            ;type carte: string de cifre
            ;param data_inceput: Data la care se face imprumutul
            ;type data_inceput: string
            ;param data_final: Data la care se va returna imprumutul
            ;type data_final: string
            ;param status: Statusul imprumutului
            ;type status: string
        """
        try:
            Validator.validare_id(client)
        except ValueError as ex:
            raise ex
        
        try:
            Validator.validare_id(carte)
        except ValueError as ex:
            raise ex
        
        try:
            Validator.validare_data(data_inceput)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_data(data_final)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_status(status)
        except ValueError as ex:
            raise ex
        
        if self.exista_imprumut(client, carte, data_inceput, data_final, status):
            raise RentAlreadyExistsException()
        
        imprumut_nou = Imprumuturi(client, carte, data_inceput, data_final, status)
        self.set_imprumuturi(imprumut_nou)

    def sterge_imprumut_book_ID(self, book_id):
        """
            Sterge imprumuturile cu id de carte dat
            ;param book_id: ID cartii
            ;type book_id: string de cifre
        """
        imprumuturi_nesterse = []
        for imprumut in self.__imprumuturi:
            if imprumut.get_imprumut_book() != book_id:
                imprumuturi_nesterse.append(imprumut)
        self.set_lista_imprumuturi(imprumuturi_nesterse)
        
    def sterge_imprumut_client_ID(self, client_id):
        """
            Sterge imprumuturile cu id de client dat
            ;param client_id: ID clientului
            ;type client_id: string de cifre
        """
        imprumuturi_nesterse = []
        for imprumut in self.__imprumuturi:
            if imprumut.get_imprumut_client() != client_id:
                imprumuturi_nesterse.append(imprumut)
        self.set_lista_imprumuturi(imprumuturi_nesterse)
        
    
class ImprumutFileRepo(ImprumutInMemoryRepo):
    def __init__(self, filename):
        """
            Constructorul clasei
            ;param filename: Numele fisierului din care se citeste
            ;type filename: string
        """
        ImprumutInMemoryRepo.__init__(self)
        self.__filename = filename
        self.incarca_din_fisier()
        
    def incarca_din_fisier(self):
        """
            Functia de incarcare din fisier
        """
        with open(self.__filename, "r") as h:
            lines = h.readlines()
            for line in lines:
                if line == '\n':
                    break
                clientID, bookID, data_inceput, data_final, status = [token.strip() for token in line.split(";")]
                ImprumutInMemoryRepo.adaugare_imprumut(self, clientID, bookID, data_inceput, data_final, status)
    
    def incarca_in_fisier(self):
        """
            Functia care stocheaza in fisier
        """
        with open(self.__filename, "w") as h:
            imprumuturi = ImprumutInMemoryRepo.get_imprumuturi(self)
            for imprumut in imprumuturi:
                imprumut_str = imprumut.get_imprumut_client() + " ; " + imprumut.get_imprumut_book() + " ; " + imprumut.get_data_inceput() + " ; " + imprumut.get_data_final() + " ; " + imprumut.get_status() + "\n"
                h.write(imprumut_str)
                
    def get_imprumuturi(self):
        return super().get_imprumuturi()
    
    def set_imprumuturi(self, imprumut_nou):
        super().set_imprumuturi(imprumut_nou)
        self.incarca_in_fisier()
        
    def set_lista_imprumuturi(self, imprumuturi_noi):
        super().set_lista_imprumuturi(imprumuturi_noi)
        self.incarca_in_fisier()
        
    def adaugare_imprumut(self, client, carte, data_inceput, data_final, status):
        super().adaugare_imprumut(client, carte, data_inceput, data_final, status)
        self.incarca_in_fisier()
        
    def sterge_imprumut_book_ID(self, book_id):
        super().sterge_imprumut_book_ID(book_id)
        self.incarca_in_fisier()

    def recursive_len(self, lst):
        return super().recursive_len(lst)

    def sterge_imprumut_client_ID(self, client_id):
        super().sterge_imprumut_client_ID(client_id)
        self.incarca_in_fisier()
       