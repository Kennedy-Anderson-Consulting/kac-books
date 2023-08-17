from kac_books.api.journal import Journal
from kac_books.api.accounts import Accounts
from kac_books.api.commodities import Commodities
from kac_books.api.prices import Prices
from kac_books.api.modification_callback import ModificationCallback

class Book(ModificationCallback):
    """API for accessing a book database"""
    
    name: str
    journal: Journal
    accounts: Accounts
    commodities: Commodities
    prices: Prices

    def __init__(self, name: str,
                 db_host: str = "localhost",
                 db_port: str = "5432"):
        """Connect to existing book database, and return Book object."""
        pass

    def commit(self):
        """Commit all changes to book database."""
        pass

    def revert(self):
        """Remove all changes, and revert to current state of database."""
        pass

    def update(self):
        """Fetch all updates from the book database."""
        pass

    def execute_sql(self, sql):
        """Execute sql command on book database, returning any response."""
        pass
        

def new_book(name: str,
             db_host: str = "localhost",
             db_port: str = "5432") -> Book:
    """Initialize new book database, and return Book object."""
    pass

def del_book(name: str, db_host: str = "localhost", db_port: str = "5432"):
    """Permanently delete book database."""
    pass
