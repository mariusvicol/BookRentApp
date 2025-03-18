from UI.console_comands import ConsolaCommands

from repository.book_repo import CarteFileRepo
from repository.client_repo import ClientFileRepo
from repository.imprumut_repo import ImprumutFileRepo
from service.client_service import ClientService
from service.imprumut_service import ImprumutService
from service.carte_service import CarteService

carti = CarteFileRepo("data\carti.txt")
clienti = ClientFileRepo("data\clienti.txt")
imprumuturi = ImprumutFileRepo("data\imprumuturi.txt")
controller_clienti = ClientService(clienti)
controller_carti = CarteService(carti)
controller_imprumuturi = ImprumutService(imprumuturi, clienti, carti)

UI = ConsolaCommands(controller_clienti, controller_carti, controller_imprumuturi)
UI.startProgram()
