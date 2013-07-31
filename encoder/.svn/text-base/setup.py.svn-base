from setuptools import setup, Extension

basedir = 'encoder/'
encode = Extension('qrcode.Encoder',
		    include_dirs = [basedir+'./src/'],
		    sources =[
			basedir+'Encoder.c',
			basedir+'./src/qrencode.c',
			basedir+'./src/bitstream.c',
			basedir+'./src/qrinput.c',
			basedir+'./src/qrspec.c',
			basedir+'./src/rscode.c'])

setup (name = 'qrcode',
	version = '0.2.1',
	description = 'Quick Response encoder and decoder.',
	author = 'Alexandre Fiori',
	author_email = 'fiorix@gmail.com',
	url = 'http://pyqrcode.sourceforge.net',
	long_description = '''Quick Response encoder and decoder.''',
	ext_modules = [encode],
	include_package_data = True,
	package_data = {'': ['*.jar']},
	packages=['qrcode'])
