class ModificationCallback:
    """tracks functions to call when database is altered"""

    def add_callback(self, callback: callable) -> int:
        """add function to call when database is altered returning key"""
        pass

    def del_callback(self, key: int):
        """remove callback idetified by key"""
        pass

    def callback(self):
        """call callback functions"""
        pass

