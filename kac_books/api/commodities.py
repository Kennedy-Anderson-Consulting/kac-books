

class Commodity:
    """fungible unit of economic value"""

    name: str
    symbol: str
    description: str
    price_commodity: Commodity

    def edit(name: str = None,
             symbol: str = None,
             description: str = None,
             price_commodity: Commodity = None):
        """edit commodity"""
        pass


class Commodities:
    """list of all commodities"""

    def add_commodity(self,
                      name: str,
                      symbol: str,
                      description: str,
                      price_commodity: Commodity):
        """add commodity"""
        pass

    def del_commodity(self, commodity: Commodity):
        """delete commodity"""
        pass

    def price_path(self,
                   price_of: Commodity,
                   price_in: Commodity) -> list[tuple[Commodity, bool]]:
        """Find intermediate prices necessary to compute relative price."""

    def __getitem__(self, index):
        """get commodity by index"""
        pass

    def __len__(self):
        """return number of commodities"""
        pass

    def __iter__(self):
        """return iterable over prices"""
        pass
