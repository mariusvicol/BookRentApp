class Client:
    def __init__(self, client_id, nume, CNP):
        self.__client_id = client_id
        self.__nume = nume
        self.__CNP = CNP
        
    def get_client_id(self):
        """
            Returneaza id-ul clientului
        """
        return self.__client_id
    
    def get_client_nume(self):
        """
            Returneaza numele clientului
        """
        return self.__nume
    
    def get_client_CNP(self):
        """
            Returneaza CNP-ul clientului
        """
        return self.__CNP
    
    def set_client_id(self, id_nou):
        """
            Seteaza id-ul clientului cu un id nou
        """
        self.__client_id = id_nou
        
    def set_client_nume(self, nume_nou):
        """
            Seteaza numele clientului cu un nume nou
        """
        self.__nume = nume_nou
        
    def set_client_CNP(self, CNP_nou):
        """
            Seteaza CNP-ul clientului cu un CNP nou
        """
        self.__CNP = CNP_nou
