import jp.sourceforge.qrcode.QRCodeDecoder;
import jp.sourceforge.qrcode.data.QRCodeImage;
import jp.sourceforge.qrcode.util.ContentConverter;
import jp.sourceforge.qrcode.exception.DecodingFailedException;

// debug?
import jp.sourceforge.qrcode.util.DebugCanvas;
import jp.sourceforge.qrcode.util.DebugCanvasAdapter;

import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;

public class Decoder {
    public String error = "";
    public String result = "";

    public boolean decode(String filename) {
	DebugCanvas canvas = new J2SECanvas();
	QRCodeDecoder decoder = new QRCodeDecoder();
	decoder.setCanvas(canvas);

	return processDecode(filename, decoder);
    }

    private boolean processDecode(String filename, QRCodeDecoder decoder) {
	try {
	    BufferedImage image = ImageIO.read(new File(filename));
	    String decodedString = new String(decoder.decode(new J2SEImage(image)));
	    result = ContentConverter.convert(decodedString);
	    error = "";
	    return true;
	} catch(IOException ioe) {
	    result = "";
	    error = ioe.getMessage();
	} catch(DecodingFailedException dfe) {
	    result = "";
	    error = dfe.getMessage();
	} catch(Exception e) {
	    result = "";
	    error = e.getMessage();
	}
	return false;
    }
}

class J2SEImage implements QRCodeImage {
    private BufferedImage image = null;

    public J2SEImage(BufferedImage source)	{ this.image = source;       }
    public int getWidth()			{ return image.getWidth();   }
    public int getHeight()			{ return image.getHeight();  }
    public int getPixel(int x, int y)		{ return image.getRGB(x, y); }
}

class J2SECanvas extends DebugCanvasAdapter {
      public void println(String s) {
	//System.err.println(s);
      }
}
