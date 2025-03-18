from domain.client import Client
from repository.validare_date import Validator
from utils.utils import deep_copy_lista
from exception.exception import ClientAlreadyExistsException

class ClientInMemoryRepo:
    def __init__(self):
        self.__clienti = []

    def get_clienti(self):
        return self.__clienti

    def set_lista_clienti(self, clienti_noi):
        self.__clienti = deep_copy_lista(clienti_noi)

    def set_clienti(self, client_nou):
        self.__clienti.append(client_nou)

    def adaugare_client_nou(self, client_id, nume, CNP):
        """
        Creaza si adauga un client nou in biblioteca
        ;param client_id: ID clientului
        ;type client_id: string de cifre
        ;param nume: Numele clientului
        ;type nume: string
        ;param CNP: CNP-ul clientului
        ;type CNP: string ce cifre
        """
        try:
            Validator.validare_id(client_id)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_nume(nume)
        except ValueError as ex:
            raise ex

        try:
            Validator.validare_CNP(CNP)
        except ValueError as ex:
            raise ex

        for client in self.__clienti:
            if client.get_client_id() == client_id or client.get_client_CNP() == CNP:
                raise ClientAlreadyExistsException()

        client_nou = Client(client_id, nume, CNP)
        self.set_clienti(client_nou)

    def sterge_clientID(self, id_client):
        """
            Sterge clientul cu ID-ul dat
            ;param client_id: ID clientului
            ;type client_id: string de cifre
        """
        clienti_nestersi = []
        for client in self.__clienti:
            if client.get_client_id() != id_client:
                clienti_nestersi.append(client)
        self.set_lista_clienti(clienti_nestersi)

    def cautare_clientID(self, clientID):
        """
            Cauta clientul dupa ID-ul citit si ii returneaza numele si CNP-ul
            ;param clientID: ID-ul clientulul cautat
            ;type clientID: string
            ;return: nume, CNP
            ;rtype: string, string
        """
        for client in self.get_clienti():
            if clientID == client.get_client_id():
                return client.get_client_nume(), client.get_client_CNP()


class ClientFileRepo(ClientInMemoryRepo):
    def __init__(self, filename):
        """
        Constructorul clasei
        :param filename: numele fisierului
        """
        ClientInMemoryRepo.__init__(self)
        self.__filename = filename
        self.__incarca_din_fisier()

    def __incarca_din_fisier(self):
        """
            Salveaza in memorie date din fisier
        """
        with open(self.__filename, "r") as g:
            lines = g.readlines()
            for line in lines:
                if line == "\n":
                    break
                clientID, nume, CNP = [token.strip() for token in line.split(";")]
                ClientInMemoryRepo.adaugare_client_nou(self, clientID, nume, CNP)

    def salveaza_in_fisier(self):
        """
            Salveaza in fisier date din memorie
        """
        with open(self.__filename, "w") as g:
            clienti = ClientInMemoryRepo.get_clienti(self)
            for client in clienti:
                client_str = client.get_client_id() + " ; " + client.get_client_nume() + " ; " + client.get_client_CNP() + "\n"
                g.write(client_str)

    def sterge_clientID(self, clientId):
        """
            Suprascrie stergere client din repo
        """
        ClientInMemoryRepo.sterge_clientID(self, clientId)
        self.salveaza_in_fisier()

    def cautare_clientID(self, clientID):
        """
            Suprascrie cautare client din repo
        """
        return ClientInMemoryRepo.cautare_clientID(self, clientID)

    def get_clienti(self):
        """
            Suprascrie get clienti din repo
        """
        return ClientInMemoryRepo.get_clienti(self)

    def set_clienti(self, client_nou):
        """
            Suprascrie set clienti din repo
        """
        ClientInMemoryRepo.set_clienti(self, client_nou)
        self.salveaza_in_fisier()

    def set_lista_clienti(self, clienti_noi):
        """
            Suprascrie set lista clienti
        """
        ClientInMemoryRepo.set_lista_clienti(self, clienti_noi)
        self.salveaza_in_fisier()

    def adaugare_client_nou(self, client_id, nume, CNP):
        ClientInMemoryRepo.adaugare_client_nou(self, client_id, nume, CNP)
        self.salveaza_in_fisier()
