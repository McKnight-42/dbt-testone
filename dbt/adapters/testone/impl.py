# adapter_src, and adapter_cls comes from kwargs in create.py
from dbt.adapters.sql import SQLAdapter
from dbt.adapters.testone import TestOneConnectionManager


class TestOneAdapter(SQLAdapter):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    ConnectionManager = TestOneConnectionManager

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "datenow()"


# may require more build out to make more user friendly to confer with team and community.
