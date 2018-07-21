
from proboscis import test

@test(groups=["unit", "numbers"])
class TestIsNegative():
    """Confirm that utils.is_negative works correctly."""

    @test(always_run=True,enabled=True)
    def TC1(self):
        print "Ran"

    @test(depends_on=[TC1],always_run=True,enabled=True)
    def TC2(self):
        print "Ran"

    @test(depends_on=[TC2],always_run=True,enabled=True)
    def TC3(self):
        print "Ran"
