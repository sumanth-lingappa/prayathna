from nose.tools import *
import os, sys
from StringIO import StringIO

import logging
logger = logging.getLogger(__name__)

import sys
sys.path.insert(0, os.path.dirname(__file__))
import logging_helper

HEADER_PAT = logging_helper.HEADER_FMT.replace("%d", "%s") % (".+", "\d+", ".+", "\d+", "\d+", "\d+")
"""The header log message pattern."""

STACK_PAT = logging_helper.STACK_FMT.replace("%d", "%s") % (".+", "\d+", ".+")
"""The stack content log message pattern."""

class TestLoggingHelper(object):
    """The logging helper unit tests."""

    def setUp(self):
        self.buffer = StringIO()
        log_handler = logging.StreamHandler(self.buffer)
        formatter = logging.Formatter("%(message)s")
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)

    def test_full_stack(self):
        self.outer()
        log = self.buffer.getvalue().splitlines()
        hdr = log.pop(0)
        assert_regexp_matches(hdr, HEADER_PAT, "Log header message incorrect")
        for msg in log:
            assert_regexp_matches(msg, STACK_PAT, "Log stack message incorrect")

    def test_partial_stack(self):
        self.outer(2, 1)
        log = self.buffer.getvalue().splitlines()
        assert_equals(3, len(log), "Log size incorrect: %d" % len(log))

    def outer(self, limit=None, start=0):
        self.middle(limit, start)

    def middle(self, limit, start):
        self.inner(limit, start)

    def inner(self, limit, start):
        logging_helper.log_stack(logger, limit, start)


if __name__ == "__main__":
    import nose

    nose.main(defaultTest=__name__)