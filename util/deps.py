#!/usr/bin/env python
# coding: utf-8
#
# pyqrcode dependency test

import sys

try:
    from jcc import initVM
except ImportError:
    print 'JCC not found.'
    sys.exit(1)

try:
    from Image import fromstring
    from ImageOps import expand
except ImportError:
    print 'PIL (python imaging) not found.'
    sys.exit(1)

try:
    from new import classobj
except ImportError:
    print 'Your python version doesn\'t support importing "new"'
    sys.exit(1)
