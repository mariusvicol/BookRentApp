from exception.exception import ClientAlreadyExistsException, BookAlreadyExistsException, RentAlreadyExistsException
from repository.imprumut_repo import ImprumutFileRepo
from utils.sortari import generic_sort
from utils.utils import creare_dicitionar


class ImprumutService:
    def __init__(self, repo, clienti, carti):
        self.__repo = repo
        self.__carti = carti
        self.__clienti = clienti

    def get_repo(self):
        return self.__repo

    def adaugare_imprumut_service(self, client, carte, data_de_inceput, data_de_final, status):
        """
        :param client: ID-ul clientului
        :param carte: ID-ul cartii
        :param data_de_inceput: Data de inceput
        :param data_de_final: Data de final
        :param status: Statusul imprumutului
        """
        self.__repo.adaugare_imprumut(client, carte, data_de_inceput, data_de_final, status)

    def get_clienti(self):
        """
            Returneaza lista de clienti
        """
        return self.__clienti

    def get_carti(self):
        """
            Returneaza lista de carti
        """
        return self.__carti

    def adaugareDefault(self):
        """
            Adauga default date in biblioteca
        """
        try:
            self.__carti.adaugare_carte_noua("1010", "Amintiri din copilarie", "scolara", "Ion Creanga")
            print("Cartea a fost adaugata cu succes.")
        except BookAlreadyExistsException as ex:
            print("Eroare la adaugarea cartii:", ex)
        try:
            self.__carti.adaugare_carte_noua("1011", "Ion", "roman", "Liviu Rebreanu")
            print("Cartea a fost adaugata cu succes.")
        except BookAlreadyExistsException as ex:
            print("Eroare la adaugarea cartii:", ex)
        try:
            self.__carti.adaugare_carte_noua("1012", "Moara cu noroc", "nuvela", "Ioan Slavici")
            print("Cartea a fost adaugata cu succes.")
        except BookAlreadyExistsException as ex:
            print("Eroare la adaugarea cartii:", ex)
        try:
            self.__clienti.adaugare_client_nou("1", "Loghin Bogdan", "1990708330531")
            print("Clientul a fost adaugat cu succes.")
        except ClientAlreadyExistsException as ex:
            print("Eroare la adaugarea clientului:", ex)
        try:
            self.__clienti.adaugare_client_nou("2", "Popescu Maria", "2870912331432")
            print("Clientul a fost adaugat cu succes.")
        except ClientAlreadyExistsException as ex:
            print("Eroare la adaugarea clientului:", ex)
        try:
            self.__clienti.adaugare_client_nou("3", "Ionescu Mihai", "1700809341442")
            print("Clientul a fost adaugat cu succes.")
        except ClientAlreadyExistsException as ex:
            print("Eroare la adaugarea clientului:", ex)
        try:
            self.__repo.adaugare_imprumut("1", "1001", "20.10.2020", "30.10.2020", "Nereturnat")
            print("Imprumutul a fost adaugat cu succes.")
        except RentAlreadyExistsException as ex:
            print("Eroare la adaugarea imprumutului:", ex)
        try:
            self.__repo.adaugare_imprumut("2", "1002", "01.11.2023", "10.11.2023", "Returnat")
            print("Imprumutul a fost adaugat cu succes.")
        except RentAlreadyExistsException as ex:
            print("Eroare la adaugarea imprumutului:", ex)
        try:
            self.__repo.adaugare_imprumut("3", "1000", "12.10.2021", "12.01.2022", "Restant")
            print("Imprumutul a fost adaugat cu succes.")
        except RentAlreadyExistsException as ex:
            print("Eroare la adaugarea imprumutului:", ex)

    def sterge_BIBLIOTECA(self):
        """
            Adauga liste noi in biblioteca
        """
        self.__carti.set_lista_carti([])
        self.__clienti.set_lista_clienti([])
        self.__repo.set_lista_imprumuturi([])

    def sterge_imprumut_DATA_INCEPUT(self, data_inceput):
        """
            Sterge imprumuturile cu data de inceput data
            param data_inceput: Data la care se face imprumutul
            ;type data_inceput: string
        """
        imprumuturi_nesterse = []
        for imprumut in self.__repo.get_imprumuturi():
            if imprumut.get_data_inceput() != data_inceput:
                imprumuturi_nesterse.append(imprumut)
        self.__repo.set_lista_imprumuturi(imprumuturi_nesterse)

    def sterge_imprumut_DATA_FINAL(self, data_final):
        """
            Sterge imprumuturile cu data de final data
            ;param data_final: Data la care se va returna imprumutul
            ;type data_final: string
        """
        imprumuturi_nesterse = []
        for imprumut in self.__repo.get_imprumuturi():
            if imprumut.get_data_final() != data_final:
                imprumuturi_nesterse.append(imprumut)
        self.__repo.set_lista_imprumuturi(imprumuturi_nesterse)

    def sterge_imprumut_STATUS(self, status):
        """
            Sterge imprumuturile cu statusul dat
            ;param status: Statusul imprumutului
            ;type status: string
        """
        imprumuturi_nesterse = []
        for imprumut in self.__repo.get_imprumuturi():
            if imprumut.get_status() != status:
                imprumuturi_nesterse.append(imprumut)
        self.__repo.set_lista_imprumuturi(imprumuturi_nesterse)

    def clienti_cu_carti_inchiriate_ordonati_dupa_nume(self):
        """
            Returneaza clientii care au inchiriat carti ordonati dupa nume
        """
        clienti_cu_carti_inchiriate = []
        for client in self.__clienti.get_clienti():
            client_id = client.get_client_id()
            carti_inchiriate = []
            for imprumut in self.__repo.get_imprumuturi():
                if imprumut.get_imprumut_client() == client_id:
                    book_id = imprumut.get_imprumut_book()
                    carti_inchiriate.append(book_id)
            if carti_inchiriate:
                clienti_cu_carti_inchiriate.append((client.get_client_nume(), carti_inchiriate))
        # clienti_cu_carti_inchiriate.sort(key=lambda x: x[0])
        clienti_cu_carti_inchiriate = generic_sort(
            clienti_cu_carti_inchiriate,
            key=lambda x: x[0],
            cmp=lambda x, y: x <= y,
            algorithm="bingo_sort"
        )

        return clienti_cu_carti_inchiriate

    def clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor(self):
        """
                Returneaza clientii care au inchiriat carti ordonati dupa numarul cartilor
            """
        clienti_cu_carti_inchiriate = []
        for client in self.__clienti.get_clienti():
            client_id = client.get_client_id()
            carti_inchiriate = []
            for imprumut in self.__repo.get_imprumuturi():
                if imprumut.get_imprumut_client() == client_id:
                    book_id = imprumut.get_imprumut_book()
                    carti_inchiriate.append(book_id)
            if carti_inchiriate:
                clienti_cu_carti_inchiriate.append((client.get_client_nume(), carti_inchiriate))
        # clienti_cu_carti_inchiriate.sort(key=lambda x: len(x[1]), reverse=True)
        clienti_cu_carti_inchiriate = generic_sort(
            clienti_cu_carti_inchiriate,
            key=lambda x: len(x[1]),
            cmp=lambda x, y: x <= y,
            reverse=True
        )
        return clienti_cu_carti_inchiriate

    def carti_inchiriate_ordonate_dupa_numarul_imprumuturilor(self):
        """
            Returneaza cartile inchiriate ordonate dupa numarul de imprumuturi

            Complexitatea functiei:
            pentru ca parcurg lista de imprumuturi complexitatea este Theta(n) unde n este numarul de imprumururi din lista
            in momentul in care fac sortarea complexitatea lui MergeSort este Theta(m*log(m)) unde m este numarul de elemente din lista pe care o sortez

            C(m) = 2*C(m/2)+m

            Continuând acest raţionament, putem scrie
            C(m) = 2*(2*C(m/4)+n/2)+m = 4C(m/4) + m + m

            Algoritmul se opreşte după log2(m) astfel de paşi, când se obţine

            C(m) = mC(m/m) + m + m + ... + m = m*log2(m)

            In consecinţă, complexitatea algoritmului de sortare MergeSort este Theta(m*log2(m)).

            Deci in final complexitatea va fi Theta(n+(m*log(m)))
        """
        carti_inchiriate = {}

        for imprumut in self.__repo.get_imprumuturi():
            book_id = imprumut.get_imprumut_book()
            if book_id in carti_inchiriate:
                carti_inchiriate[book_id] += 1
            else:
                carti_inchiriate[book_id] = 1

        carti_inchiriate_sorted = generic_sort(list(carti_inchiriate.items()), key=lambda x: x[1],
                                               cmp=lambda x, y: x <= y, reverse=True)
        # carti_inchiriate_sorted = sorted(carti_inchiriate.items(), key=lambda x: x[1], reverse=True)
        carti_inchiriate_lista = [creare_dicitionar(element[0], element[1]) for element in carti_inchiriate_sorted]

        return carti_inchiriate_lista

    def primele_10_la_suta_mai_putin_inchiriate(self):
        """
        Returneaza primele 10% dintre cele mai putin inchiriate carti,
        ordonate crescator dupa numarul de inchirieri,
        si in cadrul aceluiasi numar de inchirieri ordonate crescator dupa id
        """
        carti_inchiriate = {}

        for imprumut in self.__repo.get_imprumuturi():
            book_id = imprumut.get_imprumut_book()
            if book_id in carti_inchiriate:
                carti_inchiriate[book_id] += 1
            else:
                carti_inchiriate[book_id] = 1

        # carti_inchiriate_sorted = sorted(carti_inchiriate.items(), key=lambda x: x[1])

        carti_inchiriate_lista = generic_sort(
            list(carti_inchiriate.items()),
            key=lambda x: (x[1], x[0]),
            cmp=lambda x, y: x <= y
        )

        numar_total_carti = self.__repo.recursive_len(carti_inchiriate_lista)
        numar_carti_10_percent = int(numar_total_carti * 0.1)

        if numar_carti_10_percent == 0:
            return "Nu exista imprumuturi pentru a determina numarul de carti inchiriate."
        else:
            primele_10_percent_carti = carti_inchiriate_lista[:numar_carti_10_percent]
            return primele_10_percent_carti

    def seteaza_statusRETURNAT(self, client_id, book_id):
        """
            Seteaza statusul imprumutului la Returnat
            ;param client_id: ID-ul clientului
            ;type client_id: string
            ;param book_id: ID-ul cartii
            ;type book_id: string
        """
        for imprumut in self.__repo.get_imprumuturi():
            if imprumut.get_imprumut_client() == client_id and imprumut.get_imprumut_book() == book_id:
                imprumut.set_status("Returnat")
        if self.get_repo() == ImprumutFileRepo:
            self.__repo.incarca_in_fisier()

    def seteaza_statusNERETURNAT(self, client_id, book_id):
        """
                Seteaza statusul imprumutului la Nereturnat
                ;param client_id: ID-ul clientului
                ;type client_id: string
                ;param book_id: ID-ul cartii
                ;type book_id: string
            """
        for imprumut in self.__repo.get_imprumuturi():
            if imprumut.get_imprumut_client() == client_id and imprumut.get_imprumut_book() == book_id:
                imprumut.set_status("Nereturnat")
        if self.get_repo() == ImprumutFileRepo:
            self.__repo.incarca_in_fisier()

    def seteaza_statusRESTANT(self, client_id, book_id, imprumuturi=None, index=0):
        """
        Seteaza statusul imprumutului la Restant recursiv
        :param client_id: ID-ul clientului
        :type client_id: string
        :param book_id: ID-ul cartii
        :type book_id: string
        :param imprumuturi: Lista de imprumuturi (folosit pentru recursivitate)
        :type imprumuturi: list de obiecte Imprumut
        :param index: Indexul curent in lista de imprumuturi (folosit pentru recursivitate)
        :type index: int
        """
        if imprumuturi is None:
            imprumuturi = self.__repo.get_imprumuturi()

        if index < len(imprumuturi):
            imprumut = imprumuturi[index]
            if imprumut.get_imprumut_client() == client_id and imprumut.get_imprumut_book() == book_id:
                imprumut.set_status("Restant")

            self.seteaza_statusRESTANT(client_id, book_id, imprumuturi, index + 1)

        if self.get_repo() == ImprumutFileRepo:
            self.__repo.incarca_in_fisier()
