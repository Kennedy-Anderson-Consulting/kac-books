from datetime import date, time

from kac_books.api.modification_callback import ModificationCallback
from kac_books.api.commodity import Commodity
from kac_books.api.value import Value


class Price(ModificationCallback):
    """A price of a commodity at a date and time."""

    commodity: Commodity
    value: Value
    date: date
    time: time
    price_id: int

    def edit_price(self,
                   commodity: Commodity = None,
                   value: Value = None
                   date: date = None,
                   time: time = None):
        """set price data"""
        pass

class Prices(ModificationCallback):
    """Cronological list of all prices."""

    def last_price(self,
                   commodity: Commodity,
                   date: date = None,
                   time: time = None):
        """get most recent price of commodity before date and time"""
        pass

    def add_price(self,
                  commodity: Commodity,
                  value: Value,
                  date: date = date.today(),
                  time: time = time(23, 59, 59, 999999)):
        """create new price"""
        pass

    def del_price(self, price: Price):
        """delete price using price reference"""
        pass

    def __getitem__(self, index):
        """return price by index"""
        pass

    def __len__(self):
        """return number of prices"""
        pass

    def __iter__(self):
        """return iterable over prices"""
        pass
