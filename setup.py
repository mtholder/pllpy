from distutils.core import setup, Extension

from Cython.Distutils import build_ext
import pkg_resources
import os
data_dir = pkg_resources.resource_filename("autowrap", "data_files")

include_dirs = [data_dir]
library_dirs = ['/usr/local/lib']
PLL_INSTALL_DIR = os.environ.get('PLL_INSTALL_DIR')
if PLL_INSTALL_DIR:
    if not os.path.isdir(PLL_INSTALL_DIR):
        sys.exit('PLL_INSTALL_DIR found in env as "{}", but it is not a valid directory\n'.format(PLL_INSTALL_DIR))
    include_dirs.append(os.path.join(PLL_INSTALL_DIR, 'include'))
    library_dirs.append(os.path.join(PLL_INSTALL_DIR, 'lib'))

ext = Extension("pllpy",
                sources = ['src/pllpy.pyx', 'src/pllml.cpp'],
                language="c++",
                include_dirs=include_dirs,
                libraries=['pll-sse3-pthreads'],
                library_dirs=library_dirs,
                extra_compile_args=['-std=c++11'],
               )

setup(cmdclass={'build_ext':build_ext},
      name="pllpy",
      version="0.1.9",
      author='Kevin Gori',
      author_email='kgori@ebi.ac.uk',
      description='Wrapper for Phylogenetic Likelihood Library',
      url='https://github.com/kgori/pllpy.git',
      ext_modules = [ext],
      install_requires=[
        'autowrap',
        'cython',
      ],
      scripts=['bin/pll']
     )