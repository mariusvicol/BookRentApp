def creare_dicitionar(book_id, numar_inchirieri):
    """
        Creaza si returneaza un dicitionar
    """
    dictionar = {"book_id":book_id, "numar_inchirieri" :numar_inchirieri}
    return dictionar

def get_book_id_dict(dictionar):
    return dictionar["book_id"]

def get_numar_inchirieri(dictionar):
    return dictionar["numar_inchirieri"]

def set_numar_inchirieri(dictionar, numar_nou):
    dictionar["numar_inchirieri"] = numar_nou

def deep_copy_lista(lista):
    """
        Simulez functia deepCopy din modulul copy pentru a face deepCopy listei mele
    """
    lista_noua = []
    for element in lista:
        element_nou = element
        lista_noua.append(element_nou)
    return lista_noua

