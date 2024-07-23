from library.libraryItem import LibraryItem  # Importa a classe base LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, year, publisher, pages_number):
        super().__init__(title, "Books")  # Chama o inicializador da classe base com o título e setor
        self.author = author  # Define o autor do livro
        self.year = year  # Define o ano de publicação do livro
        self.publisher = publisher  # Define a editora do livro
        self.pages_number = pages_number  # Define o número de páginas do livro

    def __str__(self):
        # Retorna uma representação em string do objeto Book
        return f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nPublisher: {self.publisher}\nPages: {self.pages_number}'
