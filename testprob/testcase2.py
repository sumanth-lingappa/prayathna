from proboscis import test
from proboscis.asserts import assert_equal

@test(groups=["unit", "strings"])
def test_reverse():
    """Make sure our complex string reversal logic works."""
    original = "hello"
    expected = "olleh"
    actual = reversed(original)
    assert_equal(expected, actual)