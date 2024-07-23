import datetime
from library.book import Book  # Supondo que a classe Book esteja definida em um arquivo book.py
from library.magazine import Magazine  # Supondo que a classe Magazine esteja definida em um arquivo magazine.py
from library.documentary import Documentary  # Supondo que a classe Documentary esteja definida em um arquivo documentary.py

# Criando um objeto Book
book = Book("Tudo é rio", "Carla Madeira", 2021, "Record", 210)

# Chamando métodos do objeto Book
print("Book Information:")
print(book)  # Chama implicitamente o método __str__
print()

book.borrow()  # Testando emprestar o livro
print()
book.borrow()
print()
book.borrow(datetime.datetime(2024, 7, 29))

book.return_book()  # Testando retornar o livro
print()

# Criando um objeto Magazine
magazine = Magazine("National Geographic", "National Geographic Society", 120)

# Chamando métodos do objeto Magazine
print("Magazine Information:")
print(magazine)  # Chama implicitamente o método __str__
print()

magazine.add_article("Discovering the Arctic", "John Smith")  # Adicionando um artigo à revista
print(f"Articles in the magazine: {magazine.get_articles()}")
print(f"Authors of the articles: {magazine.get_authors()}")
print()

# Criando um objeto Documentary
documentary = Documentary("The Social Dilemma", "Jeff Orlowski", "Larissa Rhodes", 2020, 94)

# Chamando métodos do objeto Documentary
print("Documentary Information:")
print(documentary)  # Chama implicitamente o método __str__
print()
