"""setup"""
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
