import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-tm1640',
    py_modules=['tm1640'],
    version='1.0.0',
    description='MicroPython library for TM1640 LED driver.',
    long_description='This library lets you operate a LED matrix display module based on a TM1640 LED driver.',
    keywords='tm1640 led matrix micropython',
    url='https://github.com/mcauser/micropython-tm1640',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)