from setuptools import setup
setup(
    name="project2",
    version="0.1",
    scripts=["data2.py"],

    #in case your program needs data files
    data_files = [('.', ['data-2.csv'])],

    #project uses matplotlib so ensure that it gets install or upgraded on target machine
    install_requires = ['matplotlib', 'pandas'], 

    #metadata to display on PyPI
    author="Me",
    Description="this is an clustering program",
    keywords="clustering program scatter plot"
)