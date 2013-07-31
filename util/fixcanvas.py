#!/usr/bin/env python
# coding: utf-8
#
# it's just for removing some buggy 
# canvas debugger from the original code
#
# you won't need it. ;)

import os, sys, shutil

tmpdir = '.tmp'
canvas = 'canvas.'

def process(origfile):
    count = 0
    lineno = 0
    tempfile = tmpdir + os.path.sep + os.path.basename(origfile)

    print 'processing ' + origfile

    fx = file(tempfile, 'w')
    fd = file(origfile)
    for line in fd:
	lineno += 1
	if not line.__contains__(canvas):
	    fx.write(line)
	else:
	    count += 1
    
    fd.close()
    fx.close()
    shutil.move(tempfile, origfile)
    

def scan(path):
    for name in os.listdir(path):
	if os.path.isdir(name):
	    scan(name)
	else:
	    fullpath = path + os.path.sep + name
	    if fullpath[-5:] == '.java':
		process(fullpath)


if __name__ == '__main__':
    try:
	path = sys.argv[1]
    except:
	print 'use: %s srcdir' % sys.argv[0]
	sys.exit(1)

    os.mkdir(tmpdir)
    scan(path)
    os.rmdir(tmpdir)
