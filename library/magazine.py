from library.libraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, publisher, pages_number):
        super().__init__(title, "Magazines")  # Chama o inicializador da classe base com título e setor
        self.publisher = publisher  # Define a editora da revista
        self.pages_number = pages_number  # Define o número de páginas da revista
        self.articles = []  # Lista para armazenar os artigos da revista
        self.authors = []  # Lista para armazenar os autores dos artigos

    def add_article(self, article, author):
        # Método para adicionar um artigo à revista
        self.articles.append(article)
        self.authors.append(author)

    def get_articles(self):
        # Método para retornar a lista de artigos da revista
        return self.articles

    def get_authors(self):
        # Método para retornar a lista de autores dos artigos da revista
        return self.authors

    def __str__(self):
        # Retorna uma representação em string do objeto Magazine
        return f'Title: {self.title}\nSector: {self.sector}\nPublisher: {self.publisher}\nPages number: {self.pages_number}'

