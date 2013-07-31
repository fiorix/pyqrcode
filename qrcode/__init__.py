# coding: utf-8
# pyqrcode

import os
from new import classobj
from qrcode import _qrcode
from ImageOps import expand
from Image import fromstring
from qrcode.Encoder import _encode

# jcc stuff
__dir__ = os.path.abspath(os.path.dirname(__file__))

class JavaError(Exception):
    def getJavaException(self):
        return self.args[0]

class InvalidArgsError(Exception):
    pass

_qrcode._setExceptionTypes(JavaError, InvalidArgsError)

VERSION = "0.2.1"
CLASSPATH = [os.path.join(__dir__, "qrcode.jar")]
CLASSPATH = os.pathsep.join(CLASSPATH)


class Encoder(object):
    def __init__(self):
	__sd = lambda x: classobj('', (), x)
	self.mode = __sd(dict(NUMERIC=0, ALNUM=1, BINARY=2, KANJI=3))
	self.eclevel = __sd(dict(L=0, M=1, Q=2, H=3))
	self.width = 400
	self.border = 10
	self.version = 5
	self.case_sensitive = True

    def encode(self, text, **kw):
	border = kw.get('border', self.border)
	w = kw.get('width', self.width) - border * 2
	v = kw.get('version', self.version)
	mode = kw.get('mode', self.mode.ALNUM)
	eclevel = kw.get('eclevel', self.eclevel.L)
	case_sensitive = kw.get('case_sensitive', self.case_sensitive)

	if v > 40:
	    raise InvalidArgsError('version should be between 1 and 40')

	version, width, data = _encode(text+'\0', case_sensitive, v, eclevel, mode)
	
	rawdata = ''
	dotsize = w / width
	realwidth = width * dotsize

	for y in range(width):
	    line = ''
	    for x in range(width):
		if ord(data[y*width+x]) % 2:
		    line += dotsize * chr(0)
		else:
		    line += dotsize * chr(255)
	    lines = dotsize * line
	    rawdata += lines
	
	image = fromstring('L', (realwidth, realwidth), rawdata)
	return expand(image, border, 255)

# auto init jvm and bind Decoder
_jvm = _qrcode.initVM(classpath=CLASSPATH, vmargs='-Djava.awt.headless=true')
Decoder = _qrcode.Decoder
