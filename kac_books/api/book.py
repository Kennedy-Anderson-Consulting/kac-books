from os import system
from pathlib import Path

import psycopg
from psycopg.rows import dict_row
from psycopg.pq import TransactionStatus

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

    def __init__(self, name: str, db_port: int = 5432):
        """Connect to existing book database, and return Book object."""
        self._connection = psycopg.connect(f"dbname={name} port={db_port}",
                                           row_factory=dict_row)
        self.journal = Journal(self)
        self.accounts = Accounts(self)
        self.commodities = Commodities(self)
        self.prices = Prices(self)

    def commit(self):
        """Commit all changes to book database."""
        self._connection.commit()

    def revert(self):
        """Remove all changes, and revert to current state of database."""
        self._connection.rollback()

    def update(self):
        """Fetch all updates from the book database."""
        pass

    def execute_sql(self, query, params=None):
        """Execute sql command on book database, returning any response."""
        cursor = self._connection.cursor()
        while (self._connection.info.transaction_status
               != TransactionStatus.INTRANS):
            cursor.execute("") #BEGINs transaction block
        with self._connection.transaction():
            cursor.execute(query, params)
        if cursor.rownumber is not None:
            return cursor.fetchall()


def new_book(name: str, db_port: int = 5432) -> Book:
    """Initialize new book database, and return Book object."""
    sql_path = Path(__file__).parent / "sql"
    system(f"createdb -p {db_port} {name}")
    system(f"psql -f {sql_path}/types.sql -p {db_port} {name}")
    system(f"psql -f {sql_path}/tables.sql -p {db_port} {name}")
    system(f"psql -f {sql_path}/functions.sql -p {db_port} {name}")
    system(f"psql -f {sql_path}/triggers.sql -p {db_port} {name}")
    return Book(name, db_port)
    

def del_book(name: str, db_port: int = 5432):
    """Permanently delete book database."""
    system(f"dropdb -p {db_port} {name}")
