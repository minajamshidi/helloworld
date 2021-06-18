# Copyright (C) 2021 Mina Jamshidi
# <minajamshidi91@gmail.com>

from setuptools import setup

with open('README.md', "r") as fh:
    long_description = fh.read()

setup(
    author='Mina Jamshidi',
    author_email='minajamshidi91@gmail.com',
    name='helloworld', # this is the name that you pip install, it does not have to be the same as the module name
    version='0.0.1',  # 0.0.x implies that it is still unstable
    description='Say hello!',  # one line usually
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["helloworld"],  # the list of actual python modules
    package_dir={'': 'src'},
    classifiers=[
        "programming Language :: Python :: 3.6",
        "License :: MIT License",
        "Operating Syster :: OS Independent"
    ],
    insall_requires=[
        "numpy ~ = 1.19",
    ],
    extras_require={
        "dev": [
                "pytest>=3.7",
        ],
    },
)

