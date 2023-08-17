from enum import StrEnum

from kac_books.api.modification_callback import ModificationCallback
from kac_books.api.commodities import Commodity
from kac_books.api.value import Value

class Category(StrEnum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

class Account(ModificationCallback):
    """Account api"""

    name: str
    code: str
    description: str
    commodity: Commodity
    parent: Account
    balance: Value
    children: list[Account]
    placeholder: bool
    category: Category

    def edit(self,
             name: str = None,
             code: str = None,
             description: str = None,
             commodity: Commodity = None,
             placeholder: bool = None,
             category: Category = None):
        """edit account values"""
        pass

    def __getitem__(self, index):
        """return child account by index"""
        pass

    def __len__(self):
        """return number of direct children"""
        pass

    def __iter__(self):
        """return iterator over direct children"""
        pass

class Accounts(ModificationCallback):
    """List of top level accounts in the chart of accounts."""

    def add_account(self,
                    name: str,
                    code: str,
                    commodity: Commodity,
                    category: Category,
                    description: str = "",
                    parent: Account = None,
                    placeholder: bool = False):
        """add account to chart of accounts"""
        pass

    def del_account(self, account: Account):
        """delete account by account reference"""
        pass

    def __getitem__(self, key):
        """Get top level account by index, or any account by name."""
        pass

    def __len__(self):
        """Return number of top level accounts."""
        pass

    def __iter__(self):
        """Return iterable over top level accounts."""
        pass
