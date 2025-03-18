from repository.book_repo import CarteFileRepo
class CarteService:
    def __init__(self, repo):
        self.__repo = repo

    def get_repo(self):
        return self.__repo

    def adaugare_carte_serivce(self, bookID, titlu, descriere, autor):
        """
        :param bookID: ID-ul cartii
        :param titlu: Titul cartii
        :param descriere: Descrierea cartii
        :param autor: Autor cartii
        """
        self.__repo.adaugare_carte_noua(bookID, titlu, descriere, autor)

    def sterge_bookID(self, bookID):
        """
        :param bookID: ID-ul cartii
        """
        self.__repo.sterge_bookID(bookID)

    def cautare_carteID(self, bookID):
        """
        :param bookID: ID-ul cartii
        """
        self.__repo.cautare_carteID(bookID)

    def sterge_bookTITLU(self, titlu):
        """
            Sterge cartile cu titlul dat
            ;param titlu: Titlul cartii
            ;type titlu: string
        """
        carti_nesterse = []
        for carte in self.__repo.get_carti():
            if carte.get_titlu() != titlu:
                carti_nesterse.append(carte)
        self.__repo.set_lista_carti(carti_nesterse)

    def sterge_bookDESCRIERE(self, descriere):
        """
            Sterge cartile cu descrierea data
            ;param descriere: Descrierea cartii
            ;type descriere: string
        """
        carti_nesterse = []
        for carte in self.__repo.get_carti():
            if carte.get_descriere() != descriere:
                carti_nesterse.append(carte)
        self.__repo.set_lista_carti(carti_nesterse)

    def sterge_bookAUTOR(self, autor):
        """
            Sterge cartile cu autorul dat
            ;param autor: Autorul cartii
            ;type autor: string
        """
        carti_nesterse = []
        for carte in self.__repo.get_carti():
            if carte.get_autor() != autor:
                carti_nesterse.append(carte)
        self.__repo.set_lista_carti(carti_nesterse)

    def modificare_bookTITLU(self, carte, titlu_nou):
        """
            Cauta o carte dupa un titlu citit si modifica cu un titlu nou
            ;param titlu: Titlul cautat
            ;type titlu: string
            ;param titlu_nou: Titlul cu care va fi modificat
            ;type titlu_nou: string
        """
        carte.set_titlu(titlu_nou)
        if self.get_repo() == CarteFileRepo:
            self.__repo.incarca_carte_in_fisier()

    def modificare_bookDESCRIERE(self, carte, descriere_noua):
        """
            Cauta o carte dupa o descirere citita si modifica cu o descriere noua
            ;param descriere: Descrierea cautata
            ;type descriere: string
            ;param descriere_noua: Descrierea cu care va fi modificata
            ;type descriere_noua: string
        """
        carte.set_descriere(descriere_noua)
        if self.get_repo() == CarteFileRepo:
            self.__repo.incarca_carte_in_fisier()

    def modificare_bookAUTOR(self, carte, autor_nou):
        """
            Cauta o carte dupa un autor citit si modifica cu un autor nou
            ;param autor: Autorul cautat
            ;type autor: string
            ;param autor_nou: Autor cu care va fi modificat
            ;type autor_nou: string
        """
        carte.set_autor(autor_nou)
        if self.get_repo() == CarteFileRepo:
            self.__repo.incarca_carte_in_fisier()

    def cautare_carteDESCRIERE(self, descriere):
        """
            Cauta o carte dupa descrierea si returneaza cartea
            ;param descriere: descrierea cartii
            ;type descriere: string
            ;retrun: carte
            ;rtype: object
        """
        carte_list = []
        for carte in self.__repo.get_carti():
            if descriere == carte.get_descriere():
                carte_list.append(carte)
        return carte_list

    def cautare_carteTITLU(self, titlu):
        """
            Cauta o carte dupa titlu si returneaza cartea
            ;param titlu: titlul cartii
            ;type titlu: string
            ;retrun: carte
            ;rtype: object
        """
        carte_list = []
        for carte in self.__repo.get_carti():
            if titlu == carte.get_titlu():
                carte_list.append(carte)
        return carte_list

    def cautare_carteAUTOR(self, autor):
        """
            Cauta o carte dupa descrierea si returneaza cartea
            ;param autor: autorul cartii
            ;type autor: string
            ;retrun: carte
            ;rtype: object
        """
        carte_list = []
        for carte in self.__repo.get_carti():
            if autor == carte.get_autor():
                carte_list.append(carte)
        return carte_list
