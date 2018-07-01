from setuptools import setup, find_packages
from os.path import basename, splitext
from glob import glob


setup(name='primes',
      version='0.1',
      description='Primality checking',
      url='https://github.com/emla2805/primes',
      author='Emil Larsson',
      author_email='emil.n.larsson@gmail.com',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      include_package_data=True,
      zip_safe=False)
