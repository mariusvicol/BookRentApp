import unittest
from domain.client import Client
from repository.client_repo import ClientInMemoryRepo
from service.client_service import ClientService
from exception.exception import ClientAlreadyExistsException

class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.clienti = ClientInMemoryRepo()
        self.clienti_service = ClientService(self.clienti)
        
    def test_set_lista_clienti(self):
        clienti_noi = [Client("1", "John Popescu", "543423423343"), Client("2", "Ioana Popovici", "2990112003332")]
        self.clienti.set_lista_clienti(clienti_noi)
        assert self.clienti.get_clienti() == clienti_noi
    
    def test_set_clienti(self):
        client_nou = Client("1", "John Popescu", "5040806339222")
        self.clienti.set_clienti(client_nou)
        assert self.clienti.get_clienti() == [client_nou]
    
    def test_adaugare_client_nou(self):
        self.clienti.adaugare_client_nou("1", "Ana Popescu", "2990101330531")
        assert len(self.clienti.get_clienti()) == 1
        """
        try:
            self.clienti.adaugare_client_nou("1", "Ana Popescu", "2990101330531")
        except ClientAlreadyExistsException as e:
            assert str(e) == "Repository Exception: Clientul exista deja."
        """
        self.assertRaises(ClientAlreadyExistsException, self.clienti.adaugare_client_nou, "1", "Ana Popescu", "2990101330531")

        self.clienti.adaugare_client_nou("2", "Alina Iuliana", "6090909223222")
        assert len(self.clienti.get_clienti()) == 2
    
    def test_sterge_clientID(self):
        client1 = Client("1990101010101", "Ana Popescu", "1990101010101")
        client2 = Client("1980808080808", "Ion Ionescu", "1980808080808")
        self.clienti.set_lista_clienti([client1, client2])
        self.clienti.sterge_clientID("1990101010101")
        assert self.clienti.get_clienti() == [client2]
    
    def test_sterge_clientNUME(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])

        self.clienti_service.sterge_clientNUME("Ana Popescu")

        assert self.clienti.get_clienti() == [client2]

    def test_sterge_clientCNP(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])

        self.clienti_service.sterge_clientCNP("1990101010101")

        assert self.clienti.get_clienti() == [client2]
    
    def test_modificare_clientNUME(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])
    
        self.clienti_service.modificare_clientNUME(client1, "Ionel Popovici")
        clienti_list = self.clienti.get_clienti()
        assert clienti_list[0].get_client_nume() == "Ionel Popovici"
    
    def test_modificare_clientCNP(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])
    
        self.clienti_service.modificare_clientCNP(client1, "1990202330431")
        clienti_list = self.clienti.get_clienti()
        assert clienti_list[0].get_client_CNP() == "1990202330431"
    
    def test_cautare_clientID(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])
    
        nume, CNP = self.clienti.cautare_clientID("1")
        assert nume == "Ana Popescu"
        assert CNP == "1990101010101"
    
    def test_cautare_clientNUME(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])
    
        client_list = self.clienti_service.cautare_clientNUME("Ana Popescu")
        for client in client_list:
            assert client == client1
    
    def test_cautare_clientCNP(self):
        client1 = Client("1", "Ana Popescu", "1990101010101")
        client2 = Client("2", "Ion Ionescu", "2000101010101")
        self.clienti.set_lista_clienti([client1, client2])
    
        client = self.clienti_service.cautare_clientCNP("1990101010101")
        assert client == client1
