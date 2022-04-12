import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsTestOne(BaseSimpleMaterializations):
    pass


class TestSingularTestsTestOne(BaseSingularTests):
    pass


class TestSingularTestsEphemeralTestOne(BaseSingularTestsEphemeral):
    pass


class TestEmptyTestOne(BaseEmpty):
    pass


class TestEphemeralTestOne(BaseEphemeral):
    pass


class TestIncrementalTestOne(BaseIncremental):
    pass


class TestGenericTestsTestOne(BaseGenericTests):
    pass


class TestSnapshotCheckColsTestOne(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampTestOne(BaseSnapshotTimestamp):
    pass

class TestBaseAdapterMethodTestOne(BaseAdapterMethod):
    pass
