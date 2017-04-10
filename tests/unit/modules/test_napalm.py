# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Anthony Shaw <anthonyshaw@apache.org>`
'''

# Import Python Libs
from __future__ import absolute_import

# Import Salt Testing Libs
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.unit import TestCase, skipIf
from tests.support.mock import (
    patch,
    NO_MOCK,
    NO_MOCK_REASON
)
import salt.modules.napalm as napalm


@skipIf(NO_MOCK, NO_MOCK_REASON)
class NapalmTestCase(TestCase, LoaderModuleMockMixin):

    def setup_loader_modules(self):
        return {napalm: {}}

    def test_behaviour(self):
        #  Test inherent behaviours
        pass