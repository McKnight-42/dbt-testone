from dbt.adapters.testone.connections import TestOneConnectionManager
from dbt.adapters.testone.connections import TestOneCredentials
from dbt.adapters.testone.impl import TestOneAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import testone


Plugin = AdapterPlugin(
    adapter=TestOneAdapter,
    credentials=TestOneCredentials,
    include_path=testone.PACKAGE_PATH)
