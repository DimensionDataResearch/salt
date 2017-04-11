# -*- coding: utf-8 -*-
'''
pp_test_module execution module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PP Playground Test module

.. versionadded:: Nitrogen

:configuration:

    .. code-block:: yaml
        <your example config>

'''
# Import Python libs
from __future__ import absolute_import
import logging

# Import salt libs
import salt.utils.compat

# Import third party libs
try:
    #  Import libs...
    
    HAS_LIBS = True
    MISSING_PACKAGE_REASON = None
except ImportError as ie:
    HAS_LIBS = False
    MISSING_PACKAGE_REASON = ie.message

log = logging.getLogger(__name__)

__virtualname__ = 'pp_test_module'


def __virtual__():
    '''
    Only load this module if dependencies is installed on this minion.
    '''
    if HAS_LIBS:
        return __virtualname__
    return (False,
            'The pp_test_module execution module failed to load:'
            'import error - {0}.'.format(MISSING_PACKAGE_REASON))


def __init__(opts):
    #  Put logic here to instantiate underlying jobs/connections
    salt.utils.compat.pack_dunder(__name__)


def my_action(params):
    # Replace this with your actions
    pass