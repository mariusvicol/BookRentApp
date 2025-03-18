
class Imprumuturi:
    def __init__(self, client, carte, data_inceput, data_final, status):
        self.__client = client
        self.__carte = carte
        self.__data_inceput = data_inceput
        self.__data_final = data_final
        self.__status = status

    def __eq__(self, other):
        """
            Compara 2 obiecte
        """
        if (
            self.get_imprumut_client() == other.get_imprumut_client()
            and self.get_imprumut_book() == other.get_imprumut_book()
            and self.get_data_inceput() == other.get_data_inceput()
            and self.get_data_final() == other.get_data_final()
            and self.get_status() == other.get_status()
        ):
            return True
        return False
        
    def get_imprumut_client(self):
        """
            Returneaza id-ul clientului din imprumut
        """
        return self.__client

    def get_imprumut_book(self):
        """
            Returneaza id-ul cartii din imprumut
        """
        return self.__carte

    def get_data_inceput(self):
        """
            Returneaza data de inceput din imprumut
        """
        return self.__data_inceput

    def get_data_final(self):
        """
            Returneaza data de final din imprumut
        """
        return self.__data_final

    def get_status(self):
        """
            Returneaza status din imprumut
        """
        return self.__status

    def set_imprumut_client(self, client_nou):
        """
            Seteaza id-ul clientului cu un id nou
        """
        self.__client = client_nou

    def set_imprumut_book(self, carte_noua):
        """
            Seteaza id-ul cartii cu un id nou
        """
        self.__carte = carte_noua

    def set_data_inceput(self, data_inceput_noua):
        """
            Seteaza data de inceput cu o data noua
        """
        self.__data_inceput = data_inceput_noua

    def set_data_final(self, data_final_noua):
        """
            Seteaza data de final cu o data noua
        """
        self.__data_final = data_final_noua

    def set_status(self, status):
        """
            Seteaza statusul cu un status nou
        """
        self.__status = status

        
