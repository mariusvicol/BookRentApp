class Carte:
    def __init__(self, book_id, titlu, descriere, autor):
        self.__book_id = book_id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
        
    def get_book_id(self):
        """
            Returneaza id-ul cartii
        """
        return self.__book_id
    
    def set_book_id(self, id_nou):
        """
            Seteaza id-ul cartii cu un id nou
        """
        self.__book_id = id_nou
        
    def get_titlu(self):
        """
            Returneaza titlul cartii
        """
        return self.__titlu
    
    def set_titlu(self, titlu_nou):
        """
            Seteaza id-ul titlul cartii cu un titlu nou
        """
        self.__titlu = titlu_nou

    def get_descriere(self):
        """
            Returneaza descrierea cartii
        """
        return self.__descriere
    
    def set_descriere(self, descriere_noua):
        """
            Seteaza descrierea cartii cu o descriere noua
        """
        self.__descriere = descriere_noua
        
    def get_autor(self):
        """
            Returneaza autorul cartii
        """
        return self.__autor
    
    def set_autor(self, autor_nou):
        """
            Seteaza autorul cartii cu un autor nou
        """
        self.__autor = autor_nou
        
   