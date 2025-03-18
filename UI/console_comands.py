from UI.citiri_printari import citire_bookAUTOR, citire_bookDESCRIERE, citire_bookTITLU, citire_carte_noua
from repository.validare_date import Validator
from UI.citiri_printari import citire_clientCNP, citire_clientNUME, citire_client_nou
from UI.citiri_printari import (citire_imprumut_nou, citire_imprumutDATA_FINAL, citire_bookID, citire_clientID,
                                citire_imprumutDATA_INCEPUT, citire_imprumutSTATUS)
from utils.utils import get_book_id_dict, get_numar_inchirieri
from exception.exception import ClientAlreadyExistsException, BookAlreadyExistsException, RentAlreadyExistsException

class ConsolaCommands:
    def __init__(self, controller_client, controller_carte, controller_imprumut):
        self.__controller_client = controller_client
        self.__controller_carte = controller_carte
        self.__controller_imprumut = controller_imprumut

    def print_meniuComands(self):
        print()
        print("----- BIBLIOTECA -----")
        print()
        print("Comenzi disponibile pentru _book, _client si _rent. Adaugati sufixul dorit si dupa caz prefixul.")
        print("Sufixe : add, delete, modify, search")
        print("Prefixe:")
        print("Pentru add: _default")
        print("Pentru delete: _all")
        print("Pentru delete_book si search_book: _id, _title, _description, _autor")
        print("Pentru delete_client si search_client: _id, _name, _cnp")
        print("Pentru delele_rent: _clientid, _book_id, _startdate, _enddate, _status")
        print("Pentru modify_book: _title, _description, _autor")
        print("Pentru modify_client: _name, _cnp")
        print("Rapoarte: report_mostrent, report_namesorted, report_booknumbersorted, report_first20%, report_first10%")
        print("Status: set_status_retured, set_status_unreturned, set_status_restant")
        print("Iesire: exit")
        print()

    def adaugare_carteUI(self):
        print()
        book_id, titlu, descriere, autor = citire_carte_noua()
        print()
        if book_id is not None:
            try:
                self.__controller_carte.adaugare_carte_service(book_id, titlu, descriere, autor)
                print("Cartea a fost adaugata cu succes.")
            except BookAlreadyExistsException as ex:
                print(ex)
        print()

    def stergere_bookID_UI(self):
        print()
        book_id = citire_bookID()
        print()
        try:
            Validator.validare_id(book_id)
            if book_id is not None:
                self.__controller_carte.sterge_bookID(book_id)
                print("Cartea cu ID-ul:", book_id, "a fost stearsa.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_bookTITLU_UI(self):
        print()
        titlu = citire_bookTITLU()
        print()
        if titlu is not None:
            self.__controller_carte.sterge_bookTITLU(titlu)
            print("Cartea cu TITLUL:", titlu, "a fost stearsa.")
            print()

    def stergere_bookDESCRIERE_UI(self):
        print()
        descriere = citire_bookDESCRIERE()
        print()
        try:
            Validator.validare_descriere(descriere)
            if descriere is not None:
                self.__controller_carte.sterge_bookDESCRIERE(descriere)
                print("Cartile cu DESCRIEREA:", descriere, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_bookAUTOR_UI(self):
        print()
        autor = citire_bookAUTOR()
        print()
        try:
            Validator.validare_nume(autor)
            if autor is not None:
                self.__controller_carte.sterge_bookAUTOR(autor)
                print("Cartile cu AUTORUL:", autor, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def modificare_carteTITLU_UI(self):
        print()
        titlu = citire_bookTITLU()
        titlu_nou = citire_bookTITLU()
        print()
        carte_list = self.__controller_carte.cautare_carteTITLU(titlu)
        if titlu_nou is not None and len(carte_list) != 0:
            for carte in carte_list:
                self.__controller_carte.modificare_bookTITLU(carte, titlu_nou)
            print("Cartile cu titlul:", titlu, "au fost modificate cu titlul:", titlu_nou)
            print()
        else:
            print("Nu exista cartea cautata.")

    def modificare_carteDESCRIERE_UI(self):
        print()
        descriere = citire_bookDESCRIERE()
        descriere_noua = citire_bookDESCRIERE()
        print()
        try:
            Validator.validare_descriere(descriere)
            Validator.validare_descriere(descriere_noua)
            carte_list = self.__controller_carte.cautare_carteDESCRIERE(descriere)
            if descriere_noua is not None and len(carte_list) != 0:
                for carte in carte_list:
                    self.__controller_carte.modificare_bookDESCRIERE(carte, descriere_noua)
                print("Cartile cu descrierea:", descriere, "au fost modificate cu descrierea:", descriere_noua)
                print()
            else:
                print("Nu exista cartea cautata.")
        except ValueError as ex:
            print(ex)

    def modificare_carteAUTOR_UI(self):
        print()
        autor = citire_bookAUTOR()
        autor_nou = citire_bookAUTOR()
        print()
        try:
            Validator.validare_nume(autor)
            Validator.validare_nume(autor_nou)
            carte_list = self.__controller_carte.cautare_carteAUTOR(autor)
            if autor_nou is not None and len(carte_list) != 0:
                for carte in carte_list:
                    self.__controller_carte.modificare_bookAUTOR(carte, autor_nou)
                print("Cartile cu autorul:", autor, "au fost modificate cu autorul:", autor_nou)
                print()
            else:
                print("Nu exista cartea cautata.")
        except ValueError as ex:
            print(ex)

    def cautare_carteID_UI(self):
        print()
        bookID = citire_bookID()
        print()
        try:
            Validator.validare_id(bookID)
            if bookID is not None:
                rezultat = self.__controller_carte.cautare_carteID(bookID)
                if rezultat is not None:
                    titlu, descriere, autor = rezultat
                    print("ID-ul cautat corespunde cartii cu TITLUL:", titlu, ",DESCRIEREA:", descriere, "si AUTORUL:",
                          autor)
                    print()
                else:
                    print("Nu exista cartea cu ID-ul citit.")
        except ValueError as ex:
            print(ex)

    def cautare_carteTITLU_UI(self):
        print()
        titlu = citire_bookTITLU()
        print()
        if titlu is not None:
            carte_list = self.__controller_carte.cautare_carteTITLU(titlu)
            if len(carte_list) != 0:
                for carte in carte_list:
                    print("Cartea cu TITLUL:", titlu, "are ID-ul:", carte.get_book_id(), ", DESCRIEREA:",
                          carte.get_descriere(),
                          "si AUTORUL:", carte.get_autor())
                print()
            else:
                print("Cartea cu TITLUL:", titlu, "nu a fost gasita.")

    def cautare_carteDESCRIERE_UI(self):
        print()
        descriere = citire_bookDESCRIERE()
        print()
        if descriere is not None:
            try:
                Validator.validare_descriere(descriere)
                carte_list = self.__controller_carte.cautare_carteDESCRIERE(descriere)
                if len(carte_list) != 0:
                    for carte in carte_list:
                        print("Cartea cu DESCRIEREA:", descriere, "are ID-ul:", carte.get_book_id(), ", TITLUL:",
                              carte.get_titlu(),
                              "si AUTORUL:", carte.get_autor())
                    print()
                else:
                    print("Cartea cu DESCRIEREA:", descriere, "nu a fost gasita.")
            except ValueError as ex:
                print(ex)

    def cautare_carteAUTOR_UI(self):
        print()
        autor = citire_bookAUTOR()
        print()
        if autor is not None:
            try:
                Validator.validare_nume(autor)
                carte_list = self.__controller_carte.cautare_carteAUTOR(autor)
                if len(carte_list) != 0:
                    for carte in carte_list:
                        print("Cartea cu AUTORUL:", autor, "are ID-ul:", carte.get_book_id(), ", TITLUL:",
                              carte.get_titlu(),
                              "si DESCRIEREA:", carte.get_descriere())
                    print()
                else:
                    print("Cartea cu AUTORUL:", autor, "nu a fost gasita.")
            except ValueError as ex:
                print(ex)

    def adaugare_clientUI(self):
        """
            Apeleaza functia de adaugare client si afiseaza mesaj
        """
        print()
        client_id, nume, CNP = citire_client_nou()
        print()
        if client_id is not None:
            try:
                self.__controller_client.adaugare_client_service(client_id, nume, CNP)
                print("Clientul a fost adaugat cu succes.")
            except ClientAlreadyExistsException as ex:
                print(ex)

    def stergere_clientID_UI(self):
        print()
        client_id = citire_clientID()
        print()
        if client_id is not None:
            self.__controller_client.sterge_clientID(client_id)
            print("Clientul cu ID-ul:", client_id, "a fost sters.")
            print()

    def stergere_clientNUME_UI(self):
        print()
        nume = citire_clientNUME()
        print()
        try:
            Validator.validare_nume(nume)
            if nume is not None:
                self.__controller_client.sterge_clientNUME(nume)
                print("Clientul cu NUMELE:", nume, "a fost sters.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_clientCNP_UI(self):
        print()
        CNP = citire_clientCNP()
        print()
        try:
            Validator.validare_CNP(CNP)
            if CNP is not None:
                self.__controller_client.sterge_clientCNP(CNP)
                print("Clientul cu CNP-ul:", CNP, "a fost sters.")
                print()
        except ValueError as ex:
            print(ex)

    def modificare_clientNUME_UI(self):
        print()
        nume = citire_clientNUME()
        nume_nou = citire_clientNUME()
        print()
        try:
            Validator.validare_nume(nume)
            Validator.validare_nume(nume_nou)
            client_list = self.__controller_client.cautare_clientNUME(nume)
            if nume_nou is not None and len(client_list) != 0:
                for client in client_list:
                    self.__controller_client.modificare_clientNUME(client, nume_nou)
                print("Clientii cu numele:", nume, "au fost modificati cu numele:", nume_nou)
                print()
            else:
                print("Nu exista clientul cautat.")
        except ValueError as ex:
            print(ex)

    def modificare_clientCNP_UI(self):
        print()
        CNP = citire_clientCNP()
        CNP_nou = citire_clientCNP()
        print()
        try:
            Validator.validare_CNP(CNP)
            Validator.validare_CNP(CNP_nou)
            client = self.__controller_client.cautare_clientCNP(CNP)
            if CNP_nou is not None and client is not None:
                self.__controller_client.modificare_clientCNP(client, CNP_nou)
                print("Clientul cu CNP-ul:", CNP, "a fost modificat cu CNP-ul:", CNP_nou)
                print()
            else:
                print("Nu exista clientul cautat.")
        except ValueError as ex:
            print(ex)

    def cautare_clientID_UI(self):
        print()
        clientID = citire_clientID()
        print()
        try:
            Validator.validare_id(clientID)
            if clientID is not None:
                rezultat = self.__controller_client.get_repo().cautare_clientID(clientID)
                if rezultat is not None:
                    nume, CNP = rezultat
                    print("Clientul cu ID-ul cautat are NUMELE:", nume, "si CNP-ul:", CNP)
                    print()
                else:
                    print("Nu exista clientul cu ID-ul citit.")
        except ValueError as ex:
            print(ex)

    def cautare_clientNUME_UI(self):
        print()
        nume = citire_clientNUME()
        print()
        try:
            Validator.validare_nume(nume)
            if nume is not None:
                client_list = self.__controller_client.cautare_clientNUME(nume)
                if len(client_list) != 0:
                    for client in client_list:
                        print("Clientul cu NUMELE:", nume, "are ID_ul:", client.get_client_id(), "si CNP-ul:",
                              client.get_client_CNP())
                    print()
                else:
                    print("Nu exista clientul cu NUMELE citit.")
        except ValueError as ex:
            print(ex)

    def cautare_clientCNP_UI(self):
        print()
        CNP = citire_clientCNP()
        print()
        try:
            Validator.validare_CNP(CNP)
            if CNP is not None:
                client = self.__controller_client.cautare_clientCNP(CNP)
                if client is not None:
                    print("Clientul cu CNP-ul:", CNP, "are ID_ul:", client.get_client_id(), "si NUMELE:",
                          client.get_client_nume())
                    print()
                else:
                    print("Nu exista clientul cu NUMELE citit.")
        except ValueError as ex:
            print(ex)

    def generare_clientUI(self):
        """
            Genereaza informatiile unei carti random si adauga cartea in lista de carti
        """
        numar = int(input("Introduceti numarul de clienti random pe care vreti sa ii adaugati: "))
        print()
        for index in range(numar):
            randomID, randomNUME, randomCNP = self.__controller_client.generare_clienti()
            try:
                self.__controller_client.adaugare_client_service(randomID, randomNUME, randomCNP)
                print("Adaugarea random a fost realizata cu succes.")
            except ValueError as ex:
                print(ex)

    def adaugare_imprumutUI(self):
        print()
        client_id, book_id, data_inceput, data_final, status = citire_imprumut_nou()
        lista_id_clienti = []
        lista_id_carti = []
        for client in self.__controller_imprumut.get_clienti().get_clienti():
            lista_id_clienti.append(client.get_client_id)
        for carte in self.__controller_imprumut.get_carti().get_carti():
            lista_id_carti.append(carte.get_book_id())
        if client_id is not None and client_id in lista_id_clienti and book_id in lista_id_carti:
            try:
                self.__controller_imprumut.adaugare_imprumut_service(client_id, book_id, data_inceput, data_final, status)
                print("Imprumutul a fost adaugat cu succes.")
            except RentAlreadyExistsException as ex:
                print(ex)
        else:
            print("Nu exista clientul sau cartea in lista de clienti si carti.")
        print()

    def stergere_imprumut_client_ID_UI(self):
        print()
        client_id = citire_clientID()
        try:
            Validator.validare_id(client_id)
            if client_id is not None:
                self.__controller_imprumut.get_repo().sterge_imprumut_client_ID(client_id)
                print("Toate imprumuturile clientului cu ID-ul:", client_id, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_imprumut_book_ID_UI(self):
        print()
        book_id = citire_bookID()
        try:
            Validator.validare_id(book_id)
            if book_id is not None:
                self.__controller_imprumut.get_repo().sterge_imprumut_book_ID(book_id)
                print("Toate imprumuturile in care apare carte cu ID-ul:", book_id, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_imprumut_DATA_INCEPUT_UI(self):
        print()
        data_inceput = citire_imprumutDATA_INCEPUT()
        try:
            Validator.validare_data(data_inceput)
            if data_inceput is not None:
                self.__controller_imprumut.sterge_imprumut_DATA_INCEPUT(data_inceput)
                print("Toate imprumuturile care au DATA DE INCEPUT:", data_inceput, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_imprumut_DATA_FINAL_UI(self):
        print()
        data_final = citire_imprumutDATA_FINAL()
        try:
            Validator.validare_data(data_final)
            if data_final is not None:
                self.__controller_imprumut.sterge_imprumut_DATA_FINAL(data_final)
                print("Toate imprumuturile care au DATA DE FINAL:", data_final, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def stergere_imprumut_STATUS_UI(self):
        print()
        status = citire_imprumutSTATUS()
        try:
            Validator.validare_status(status)
            if status is not None:
                self.__controller_imprumut.sterge_imprumut_STATUS(status)
                print("Toate imprumuturile care au STATUSUL:", status, "au fost sterse.")
                print()
        except ValueError as ex:
            print(ex)

    def seteaza_statusRETURNAT_UI(self):
        print()
        client_id = citire_clientID()
        book_id = citire_bookID()
        if client_id is not None and book_id is not None:
            self.__controller_imprumut.seteaza_statusRETURNAT(client_id, book_id)
            print("Imprumutul cu client ID:", client_id, " si book ID:", book_id, " a fost setat pe Returnat")
            print()

    def seteaza_statusNERETURNAT_UI(self):
        print()
        client_id = citire_clientID()
        book_id = citire_bookID()
        if client_id is not None and book_id is not None:
            self.__controller_imprumut.seteaza_statusNERETURNAT(client_id, book_id)
            print("Imprumutul cu client ID:", client_id, " si book ID:", book_id, " a fost setat pe Nereturnat")
            print()

    def seteaza_statusRESTANT_UI(self):
        print()
        client_id = citire_clientID()
        book_id = citire_bookID()
        if client_id is not None and book_id is not None:
            self.__controller_imprumut.seteaza_statusRESTANT(client_id, book_id)
            print("Imprumutul cu client ID:", client_id, " si book ID:", book_id, " a fost setat pe Restant")
            print()

    def adaugareDefaultUI(self):
        self.__controller_imprumut.adaugareDefault()
        print("Adaugarea default a fost realizata cu succes.")

    def stergere_BIBLIOTECA_UI(self):
        print()
        self.__controller_imprumut.sterge_BIBLIOTECA()
        print("Biblioteca a fost stearsa.")
        print()

    def cele_mai_inchiriate_cartiUI(self):
        print("Cartile inchiriate ordonate dupa numarul de imprumuturi sunt:")
        print()
        carti_inchiriate_ordonate = self.__controller_imprumut.carti_inchiriate_ordonate_dupa_numarul_imprumuturilor()

        if not carti_inchiriate_ordonate:
            print("Nu exista carti inchiriate.")
        else:
            for index in range(min(10, len(carti_inchiriate_ordonate))):
                book_id = get_book_id_dict(carti_inchiriate_ordonate[index])
                numar_imprumuturi = get_numar_inchirieri(carti_inchiriate_ordonate[index])
                print("Cartea ", index + 1, ": cu ID-ul", book_id, "a fost inchiriata de :", numar_imprumuturi, "ori.")

    def clienti_cu_carti_ordonati_dupa_numeUI(self):
        print("Clientii cu carti inchiriate ordonati dupa nume sunt:")
        print()
        clienti_ordonati_nume = self.__controller_imprumut.clienti_cu_carti_inchiriate_ordonati_dupa_nume()
        print(clienti_ordonati_nume)

    def clienti_cu_carti_ordonati_dupa_numarul_cartilorUI(self):
        print("Clientii cu carti inchiriate ordonati dupa numarul cartilor inchiriate sunt:")
        print()
        clienti_ordonati_numar_carti = self.__controller_imprumut.clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor()
        print(clienti_ordonati_numar_carti)

    def primii_cei_mai_activi_clientiUI(self):
        print("Cei mai activi 20% dintre clienti sunt: ")
        print()
        clienti_ordonati_numar_carti = self.__controller_imprumut.clienti_cu_carti_inchiriate_ordonati_dupa_numarul_cartilor()

        lungimea = len(clienti_ordonati_numar_carti)
        lungimea_noua = int(0.2 * lungimea)
        if lungimea_noua != 0:
            for index in range(lungimea_noua):
                client = clienti_ordonati_numar_carti[index]
                nume_client = client[0]
                carti_inchiriate = client[1]
                print("Clientul", index + 1, ":", nume_client, "- Carti inchiriate:", carti_inchiriate)
        else:
            print("Nu avem destule carti pentru a afisa.")

    def primele_10_la_suta_cele_mai_putin_inchiriateUI(self):
        print("Cele mai putin 10% inchiriate carti:")
        primele_10_la_suta_carti = self.__controller_imprumut.primele_10_la_suta_mai_putin_inchiriate()
        print(primele_10_la_suta_carti)

    def afisare_bibliotecaUI(self):
        """
                Afiseaza toata biblioteca
        """
        print("Biblioteca este: ")
        print()
        print("Cărți:")
        for carte in self.__controller_imprumut.get_carti().get_carti():
            print("ID:", carte.get_book_id(), "| Titlu:", carte.get_titlu(), "| Descriere:", carte.get_descriere(),
                  "| Autor:", carte.get_autor())

        print("\nClienți:")
        for client in self.__controller_imprumut.get_clienti().get_clienti():
            print("ID Client:", client.get_client_id(), "| Nume:", client.get_client_nume(), "| CNP:",
                  client.get_client_CNP())

        print("\nÎmprumuturi:")
        for imprumut in self.__controller_imprumut.get_repo().get_imprumuturi():
            nume_client = []
            for client in self.__controller_imprumut.get_clienti().get_clienti():
                if client.get_client_id() == imprumut.get_imprumut_client():
                    nume_client = client.get_client_nume()
            print("ID Client:", imprumut.get_imprumut_client(), "| Nume Client:", nume_client, "| ID Carte:",
                  imprumut.get_imprumut_book(), "| Data început:", imprumut.get_data_inceput(), "| Data final:",
                  imprumut.get_data_final(), "| Status:", imprumut.get_status())
        print()

    def startProgram(self):
        while True:
            self.print_meniuComands()
            print("Introduceti o comanda:")
            option = input("     > ")
            option = option.lower()
            option = option.strip()
            match option:
                case "add_default":
                    self.adaugareDefaultUI()

                case "add_book":
                    self.adaugare_carteUI()

                case "add_client":
                    self.adaugare_clientUI()

                case "add_rent":
                    self.adaugare_imprumutUI()

                case "delete_all":
                    self.stergere_BIBLIOTECA_UI()

                case "delete_book_id":
                    self.stergere_bookID_UI()

                case "delete_book_titlu":
                    self.stergere_bookTITLU_UI()

                case "delete_book_description":
                    self.stergere_bookDESCRIERE_UI()

                case "delete_book_autor":
                    self.stergere_bookAUTOR_UI()

                case "delete_client_id":
                    self.stergere_clientID_UI()

                case "delete_client_name":
                    self.stergere_clientNUME_UI()

                case "delete_client_cnp":
                    self.stergere_clientCNP_UI()

                case "delete_rent_clientid":
                    self.stergere_imprumut_client_ID_UI()

                case "delete_rent_bookid":
                    self.stergere_imprumut_book_ID_UI()

                case "delete_rent_startdate":
                    self.stergere_imprumut_DATA_INCEPUT_UI()

                case "delete_rent_enddate":
                    self.stergere_imprumut_DATA_FINAL_UI()

                case "delete_rent_status":
                    self.stergere_imprumut_STATUS_UI()

                case "modify_book_title":
                    self.modificare_carteTITLU_UI()

                case "modify_book_description":
                    self.modificare_carteDESCRIERE_UI()

                case "modify_book_autor":
                    self.modificare_carteAUTOR_UI()

                case "modify_client_name":
                    self.modificare_clientNUME_UI()

                case "modify_client_cnp":
                    self.modificare_clientCNP_UI()

                case "search_book_id":
                    self.cautare_carteID_UI()

                case "search_book_title":
                    self.cautare_carteTITLU_UI()

                case "search_book_desciption":
                    self.cautare_carteDESCRIERE_UI()

                case "search_book_autor":
                    self.cautare_carteAUTOR_UI()

                case "search_client_id":
                    self.cautare_clientID_UI()

                case "search_client_nume":
                    self.cautare_clientNUME_UI()

                case "search_client_cnp":
                    self.cautare_clientCNP_UI()

                case "set_status_returned":
                    self.seteaza_statusRETURNAT_UI()

                case "set_status_unreturned":
                    self.seteaza_statusNERETURNAT_UI()

                case "set_status_restant":
                    self.seteaza_statusRESTANT_UI()

                case "report_mostrent":
                    self.cele_mai_inchiriate_cartiUI()

                case "report_namesorted":
                    self.clienti_cu_carti_ordonati_dupa_numeUI()

                case "report_booknumbersorted":
                    self.clienti_cu_carti_ordonati_dupa_numarul_cartilorUI()

                case "report_first20%":
                    self.primii_cei_mai_activi_clientiUI()

                case "report_first10%":
                    self.primele_10_la_suta_cele_mai_putin_inchiriateUI()

                case "random_entities":
                    self.generare_clientUI()

                case "print":
                    self.afisare_bibliotecaUI()

                case "exit":
                    print("Va multumim!")
                    break

                case _:
                    print("Nu avem optiunea selectata")
                    print()
                    print("Va rugam alegeti o optiune valida")
