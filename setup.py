#from distutils.core import setup
#from distutils.core import setup, Extension
try:
        from setuptools import setup,Extension, find_packages
        PKGS = find_packages(where="./pyfm")
except ImportError:
        from distutils.core import setup, Extension
        PKGS = ['pyfm']
from Cython.Distutils import build_ext
from numpy.distutils.misc_util import Configuration
import numpy

setup(
	maintainer='Corey Lynch',
    name='pyfm',
    packages = PKGS,
    package_dir={'':'.'},
    url='https://github.com/coreylynch/pyFM',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("pyfm.pyfm_fast", ["pyfm_fast.pyx"],
                                                libraries=["m"],
                                                include_dirs=[numpy.get_include()])]
)
