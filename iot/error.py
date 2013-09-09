# -*- test-case-name: twisted.web.test.test_error -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Exception definitions for L{twisted.web}.
"""

import operator, warnings

#import iot.coap


class NoResource(Exception):
    """
    Raised when resource is not found.
    """

class UnallowedMethod(Exception):
    """
    Raised by a resource when request method is understood by the server 
    but not allowed for that particular resource.
    """

class UnsupportedMethod(Exception):
    """
    Raised when request method is not understood by the server at all.
    """


__all__ = [
 'UnallowedMethod', 'UnsupportedMethod'
]