"""setup.py
Here we have the name of the package: 'submit'
The python modules we're installing: 'simple', 'submit'
and also, entry points which give command line calls: 'simple', 'submit'
To use, from the directory containing this file:

pip install -e .

NB: the -e flag (editable) allows user changes to the package on disk.
"""
from setuptools import setup

setup(name='submit',
      version='0.1',
      description='Submit to HPC.',
      author='Dave Greenwood',
      py_modules=['simple', 'submit'],
      zip_safe=False,
      entry_points={'console_scripts': [
          'simple=simple:main',
          "submit=submit:main"
      ]}
      )
