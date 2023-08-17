from decimal import Decimal

from kac_books.api.commodities import Commodity

class ValueNumericOperators:
    """implements most numeric operators for type 'Value'"""

    def __init_subclass__(cls, /, **kwargs):
        """initializes numeric operators for type 'Value'"""
        pass

class Value(ValueNumericOperators):
    """immutable, quantity of a commodity that can be used in arithmetic"""

    quantity: Decimal
    commodity: Commodity

    def __init__(self, quantity, commodity: Commodity):
        """publicly accessable constructor"""
        pass
