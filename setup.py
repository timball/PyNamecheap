import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS = [
        'requests',
        'xml'
]

setup(
    name='PyNamecheap',
    version='0.1',
    long_description=README,
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    license='none yet',
    url='https://github.com/Bemmu/PyNamecheap',
    author='Bemmu Sepponen',
    author_email='me@bemmu.com',
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ]
)
