class RepositoryException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "Repository Exception: " + self.msg

class ClientAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Clientul exista deja.")

class BookAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Cartea exista deja.")

class RentAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Imprumutul exista deja")