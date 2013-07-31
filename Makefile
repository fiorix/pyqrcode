VERSION = 0.2.1
BASEPATH = decoder
LIBPATH = qrcode
SOURCEPATH = $(BASEPATH)/src
CLASSPATH = $(BASEPATH)/classes
LIBFILE = $(LIBPATH)/qrcode.jar
SRC = $(SOURCEPATH)/net/sourceforge/pyqrcode/Decoder.java

GENERATE=python -m jcc --jar $(LIBFILE) \
	    --python qrcode --version $(VERSION) --files 1 \
	    --exclude jp.sourceforge.qrcode.QRCodeDecoder \
	    --exclude jp.sourceforge.qrcode.reader.QRCodeDataBlockReader \
	    --exclude jp.sourceforge.qrcode.reader.QRCodeImageReader \
	    --exclude jp.sourceforge.qrcode.pattern.AlignmentPattern \
	    --exclude jp.sourceforge.qrcode.pattern.FinderPattern \
	    --exclude jp.sourceforge.qrcode.pattern.LogicalSeed \
	    --exclude jp.sourceforge.qrcode.geom.Axis \
	    --exclude jp.sourceforge.qrcode.geom.Line \
	    --exclude jp.sourceforge.qrcode.geom.Point \
	    --exclude jp.sourceforge.qrcode.geom.SamplingGrid \
	    --exclude jp.sourceforge.qrcode.util.ContentConverter \
	    --exclude jp.sourceforge.qrcode.util.DebugCanvas \
	    --exclude jp.sourceforge.qrcode.util.DebugCanvasAdapter \
	    --exclude jp.sourceforge.qrcode.util.QRCodeUtility \
	    --exclude jp.sourceforge.qrcode.exception.AlignmentPatternNotFoundException \
	    --exclude jp.sourceforge.qrcode.exception.InvalidDataBlockException \
	    --exclude jp.sourceforge.qrcode.exception.SymbolNotFoundException \
	    --exclude jp.sourceforge.qrcode.exception.DecodingFailedException \
	    --exclude jp.sourceforge.qrcode.exception.InvalidVersionException \
	    --exclude jp.sourceforge.qrcode.exception.VersionInformationException \
	    --exclude jp.sourceforge.qrcode.exception.FinderPatternNotFoundException \
	    --exclude jp.sourceforge.qrcode.exception.InvalidVersionInfoException \
	    --exclude jp.sourceforge.qrcode.ecc.BCH15_5 \
	    --exclude jp.sourceforge.qrcode.data.QRCodeImage \
	    --exclude jp.sourceforge.qrcode.data.QRCodeSymbol \
	    --exclude jp.sourceforge.reedsolomon.Galois \
	    --exclude jp.sourceforge.reedsolomon.RsDecode 

lib: $(SRC)
	python util/deps.py
	javac -d $(CLASSPATH) -sourcepath $(SOURCEPATH) $<
	jar cvf $(LIBFILE) -C $(CLASSPATH) .
	$(GENERATE) --build
	python encoder/setup.py build

egg: lib
	python encoder/setup.py bdist_egg

install: lib
	python encoder/setup.py install

all: lib

clean:
	rm -rf $(CLASSPATH)/* $(LIBFILE) build dist qrcode.egg-info
