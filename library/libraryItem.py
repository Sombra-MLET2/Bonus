from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC): #Tornando a classe abstrata
    @abstractmethod
    def __init__(self, title, sector):
        # Inicializador da classe LibraryItem
        self.title = title  # Define o título do item da biblioteca
        self.sector = sector  # Define o setor ao qual o item pertence na biblioteca
        self._available = True  # Define se o item está disponível para empréstimo
        self._return_date = None  # Data de retorno esperada para o item
        self._schedule_date = None  # Data agendada para empréstimo do item

    def borrow(self, requested_date=None):
        # Método para emprestar o item da biblioteca
        if requested_date is None:
            requested_date = datetime.now()  # Se a data de solicitação não for fornecida, usa a data atual

        if self._available or self._return_date > requested_date:
            # Se o item estiver disponível para empréstimo ou a data de retorno for posterior à data solicitada
            self._available = False  # Define o item como não disponível para empréstimo
            self._return_date = (datetime.now() + timedelta(days=7))  # Define a data de retorno para 7 dias após a data atual
            print(f'The book {self.title} has been borrowed successfully. The return date is {self._return_date}')
        elif self._return_date < requested_date:
            # Se a data de retorno for anterior à data solicitada (item agendado para empréstimo)
            self._schedule_date = requested_date  # Define a data agendada para empréstimo
            print(f'The book {self.title} has been scheduled successfully. The borrow date is {self._schedule_date}')
        else:
            # Se o item já estiver emprestado até a data de retorno
            print(f'The book {self.title} is already borrowed until {self._return_date}')

    def return_book(self):
        # Método para retornar o item à biblioteca
        if self._schedule_date is None:
            # Se não há data agendada para empréstimo
            self._return_date = None  # Limpa a data de retorno
            self._available = True  # Define o item como disponível novamente para empréstimo
            print(f'The book {self.title} has been returned successfully.')
        else:
            # Se há uma data agendada para empréstimo
            self._return_date = (self._schedule_date + timedelta(days=7))  # Define a nova data de retorno
            self._available = False  # Define o item como não disponível (em agendamento)
            print(f'The book {self.title} has been returned successfully.')
