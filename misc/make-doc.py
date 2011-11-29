#!/usr/bin/python
#
#     Copyright 2011, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     If you submit Kay Hayen patches to this software in either form, you
#     automatically grant him a copyright assignment to the code, or in the
#     alternative a BSD license to the code, should your jurisdiction prevent
#     this. Obviously it won't affect code that comes to him indirectly or
#     code you don't submit to him.
#
#     This is to reserve my ability to re-license the code at any time, e.g.
#     the PSF. With this version of Nuitka, using it for Closed Source will
#     not be allowed.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#     Please leave the whole of this copyright notice intact.
#

import os, sys, shutil, re

assert 0 == os.system( "rst2pdf README.txt" )

assert 0 == os.system( "python misc/gist/rst2html.py README.txt README.html" )

if not os.path.exists( "man" ):
    os.mkdir( "man" )

assert 0 == os.system( "help2man --no-discard-stderr --no-info --include doc/nuitka-man-include.txt nuitka >doc/nuitka.1" )
assert 0 == os.system( "help2man --no-discard-stderr --no-info nuitka-python >doc/nuitka-python.1" )

assert 0 == os.system( "man2html doc/nuitka.1 >doc/man-nuitka.html" )
assert 0 == os.system( "man2html doc/nuitka-python.1 >doc/man-nuitka-python.html" )

def getFile( filename ):
    return open( filename ).read()

contents = getFile( "doc/man-nuitka.html" )
new_contents = contents[ : contents.rfind( "<HR>" ) ] + contents[ contents.rfind( "</BODY>" ) : ]
assert new_contents != contents

open( "doc/man-nuitka.html", "w" ).write( new_contents )

contents = getFile( "doc/man-nuitka-python.html" )
new_contents = contents[ : contents.rfind( "<HR>" ) ] + contents[ contents.rfind( "</BODY>" ) : ]
assert new_contents != contents

open( "doc/man-nuitka-python.html", "w" ).write( new_contents )