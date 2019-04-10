#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
packages=['RQT_GUI'],
package_dir={'': 'src'},
scripts=['scripts/RQT_GUI'],
)
setup(**d)