from kac_books.api.modification_callback import ModificationCallback
from kac_books.api.value import Value
from kac_books.api.accounts import Account
from datetime import date

class Split(ModificationCallback):
    """Single split data"""

    split_id: int
    entry: 'Entry'
    account: Account
    memo: str
    value: Value


class Entry(ModificationCallback):
    """Single transaction data."""

    transaction_id: int
    date: date
    description: str
    splits: list[Split]

    def edit(self,
             date: date = None,
             description: str = None,
             add_splits: list[dict] = [],
             edit_splits: list[dict] = [],
             del_splits: list[Split] = []):
        """modify entry"""
        pass

class Journal(ModificationCallback):
    """General Journal containing all accounting transactions."""

    entries: list[Entry]
    """Cronological list of entries"""

    def add_entry(self,
                  date: date = date.today(),
                  description: str = "",
                  splits: list[dict] = []):
        """Add entry to journal"""
        pass

    def del_entry(self, entry: Entry):
        """Delete entry using entry reference"""
        pass
