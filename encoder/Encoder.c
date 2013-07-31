#include <Python.h>
#include <stdio.h>

#include "qrencode.h"

//#define MAX_DATA_SIZE 7090 /* from the specification */

static PyObject *Encoder(PyObject *self, PyObject *args)
{
    int casesensitive, en_version, v0, v1, stringsize;
    QRecLevel en_level = QR_ECLEVEL_L;
    QRencodeMode en_hint = QR_MODE_8;

    QRcode *code;
    int version, width;
    char *string;
    unsigned char *bindata;

    //buffer = (char *)malloc(MAX_DATA_SIZE);
    //buffer[ret] = '\0';

    if (!PyArg_ParseTuple(args, "s#iiii", &string, &stringsize, &casesensitive, &en_version, &v0, &v1))
        return NULL;

    if (casesensitive)
        code = QRcode_encodeStringCase(string, en_version, en_level);
    else
        code = QRcode_encodeString(string, en_version, en_level, en_hint);
    version = code->version;
    width = code->width;
    bindata = code->data;

    //QRcode_free(code);
    return Py_BuildValue("(iis)",version,width,bindata);
};

static PyMethodDef Qr_encodeMethods[] =
{
    {"_encode", Encoder, METH_VARARGS,
     "Encodes given string into QR code. Return value is a string containing RGB RAW image data."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initEncoder(void)
{
    (void) Py_InitModule("Encoder", Qr_encodeMethods);
}
