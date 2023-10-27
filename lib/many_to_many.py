import ipdb
class Author:
    all = []
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.author == self]
    
    def books(self):
        return [contracts.book for contracts in Contract.all if contracts.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contracts in Contract.all:
            if contracts.author == self:
                total += contracts.royalties
        return total

    





class Book:
    all = []
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.book == self]
    
    def authors(self):
        return [contracts.author for contracts in Contract.all if contracts.book == self]
    



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.royalties = royalties
        self.date = date
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contracts for contracts in cls.all if contracts.date == date]

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

