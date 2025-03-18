import random
import string
from repository.client_repo import ClientFileRepo

class ClientService:
    def __init__(self, repo):
        self.__repo = repo

    def get_repo(self):
        return self.__repo

    def sterge_clientID(self, clientID):
        self.__repo.sterge_clientID(clientID)

    def cautare_clientID(self, clientID):
        self.__repo.cautare_clientID(clientID)

    def adaugare_client_service(self, clientID, nume, CNP):
        """
        :param clientID: ID-ul clientului
        :param nume: nume clientului
        :param CNP: CNP clientului
        """
        self.__repo.adaugare_client_nou(clientID, nume, CNP)

    def sterge_clientNUME(self, nume):
        """
            Sterge clientul cu numele dat
            ;param nume: Numele clientului
            ;type nume: string
        """
        clienti_nestersi = []
        for client in self.__repo.get_clienti():
            if client.get_client_nume() != nume:
                clienti_nestersi.append(client)
        self.__repo.set_lista_clienti(clienti_nestersi)

    def sterge_clientCNP(self, CNP):
        """
            Sterge clientul cu CNP-ul dat
            ;param CNP: CNP-ul clientului 
            ;type CNP: string ce cifre
        """
        clienti_nestersi = []
        for client in self.__repo.get_clienti():
            if client.get_client_CNP() != CNP:
                clienti_nestersi.append(client)
        self.__repo.set_lista_clienti(clienti_nestersi)

    def modificare_clientNUME(self, client, nume_nou):
        """
            Cauta un client dupa nume si in modifica cu numele nou
            ;param nume: Numele clientului cautat
            ;type nume: string
            ;param nume_nou: Numele cu care se va modifica clientul
            ;type nume_nou: string
        """
        client.set_client_nume(nume_nou)
        if self.get_repo() == ClientFileRepo:
            self.__repo.salveaza_in_fisier()

    def modificare_clientCNP(self, client, CNP_nou):
        """
            Cauta un client dupa CNP si in modifica cu CNP nou
            ;param CNP: CNP-ul clientului cautat
            ;type CNP: string
            ;param CNP_nou: CNP-ul cu care se va modifica clientul
            ;type CNP_nou: string
        """
        client.set_client_CNP(CNP_nou)
        if self.get_repo() == ClientFileRepo:
            self.__repo.salveaza_in_fisier()

    def cautare_clientNUME(self, nume):
        """
            Cauta clientul dupa nume
            :param nume: Numele clientului cautat
            :return: Clientul gasit sau None daca nu exista
        """
        client_list = []
        for client in self.__repo.get_clienti():
            if nume == client.get_client_nume():
                client_list.append(client)
        return client_list

    def cautare_clientCNP(self, CNP):
        """
            Cauta clientul dupa CNP
            :param CNP: CNP clientului cautat
            :return: Clientul gasit sau None daca nu exista
        """
        for client in self.__repo.get_clienti():
            if CNP == client.get_client_CNP():
                return client
        return None

    def generare_clienti(self):

        randomID = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        prima_litera_nume = random.choice(string.ascii_uppercase)
        litere_mici_nume = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        randomNUME = prima_litera_nume + litere_mici_nume
        prima_litera_prenume = random.choice(string.ascii_uppercase)
        litere_mici_prenume = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))
        randomPRENUME = prima_litera_prenume + litere_mici_prenume
        randomNUMELE = randomNUME + " " + randomPRENUME

        prima_cifra = str(random.choice([1, 2, 5, 6]))
        anul = str(random.randint(0, 99)).zfill(2)
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 31)).zfill(2)
        restul = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        CNP = prima_cifra + anul + month + day + restul
        return randomID, randomNUMELE, CNP
