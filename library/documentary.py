from library.libraryItem import LibraryItem


class Documentary(LibraryItem):
    def __init__(self, title, director, producer, year, duration):
        super().__init__(title, "Documentaries")  # Chama o inicializador da classe base com título e setor
        self.director = director  # Define o diretor do documentário
        self.producer = producer  # Define o produtor do documentário
        self.year = year  # Define o ano de lançamento do documentário
        self.duration = duration  # Define a duração do documentário em minutos

    def __str__(self):
        # Retorna uma representação em string do objeto Documentary
        return f'Title: {self.title}\nSector: {self.sector}\nDirector: {self.director}\nYear: {self.year}\nProducer: {self.producer}\nDuration: {self.duration} minutes'
