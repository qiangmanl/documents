from distutils.core import setup
from setuptools import find_packages
 
setup(name = 'server',  #package name   
      version = '0.0.2',  
      description = '',
      long_description = '',
      author = 'Tao',
      author_email = 'qiangmanl@gmail.com',
      url = 'https://github.com/qiangmanl/pico-test.git',
      license = 'MIT',
      install_requires = [],
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Finance'
      ],
      keywords = '',
      packages = find_packages('src'),  
      package_dir = {'':'src'},         
      include_package_data = True
)
