## ----------------------------------------------------------------------------
##
##   File: setup.py
##   Copyright (c) <2013> <University of Paderborn>
##   Permission is hereby granted, free of charge, to any person
##   obtaining a copy of this software and associated documentation
##   files (the "Software"), to deal in the Software without restriction,
##   including without limitation the rights to use, copy, modify and
##   merge the Software, subject to the following conditions:
##
##   1.) The Software is used for non-commercial research and
##       education purposes.
##
##   2.) The above copyright notice and this permission notice shall be
##       included in all copies or substantial portions of the Software.
##
##   3.) Publication, Distribution, Sublicensing, and/or Selling of
##       copies or parts of the Software requires special agreements
##       with the University of Paderborn and is in general not permitted.
##
##   4.) Modifications or contributions to the software must be
##       published under this license. The University of Paderborn
##       is granted the non-exclusive right to publish modifications
##       or contributions in future versions of the Software free of charge.
##
##   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
##   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
##   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
##   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
##   HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
##   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
##   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
##   OTHER DEALINGS IN THE SOFTWARE.
##
##   Persons using the Software are encouraged to notify the
##   Department of Communications Engineering at the University of Paderborn
##   about bugs. Please reference the Software in your publications
##   if it was used for them.
##
##
##   Author: Jahn Heymann
##
## ----------------------------------------------------------------------------

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os
from subprocess import Popen
import shutil

try:
    shutil.rmtree('nhpylm/c_core/NHPYLM/build')
except FileNotFoundError:
    pass

os.mkdir('nhpylm/c_core/NHPYLM/build')
p = Popen(['cmake', '..'], cwd='nhpylm/c_core/NHPYLM/build')
p.wait()
p = Popen(['make'], cwd='nhpylm/c_core/NHPYLM/build')
p.wait()

setup(
    name='nhpylm',
    version='1.0b',
    description='Nested hierarchical Pitman-Yor language model',
    packages=[
        'nhpylm',
        'nhpylm.c_core'
    ],
    ext_modules = cythonize([Extension(
            "nhpylm.c_core.nhpylm", ["nhpylm/c_core/nhpylm.pyx"], language='c++',
            include_dirs=['nhpylm/c_core/NHPYLM/',
                          'nhpylm/c_core/NHPYLM/ext_deps'],
            library_dirs=['nhpylm/c_core/NHPYLM/build'],
            extra_compile_args=['-std=c++11'],
            libraries=['NHPYLM']
    )], annotate=True)
)