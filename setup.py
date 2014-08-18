import os
from setuptools import setup


def read(fname):
    inf = open(os.path.join(os.path.dirname(__file__), fname))
    out = "\n" + inf.read().replace("\r\n", "\n")
    inf.close()
    return out


setup(
    name='simpledb',
    version="1.0",
    description='Simple wrapper around SQLalchemy',
    long_description=read('README.md'),
    install_requires=["sqlalchemy>=0.6.6"],
    keywords='sqlalchemy database',
    author='Sridhar Ratnakumar',
    author_email='github@srid.name',
    url='http://github.com/ActiveState/simpledb',
    license='MIT',
    py_modules=["simpledb"],
)
