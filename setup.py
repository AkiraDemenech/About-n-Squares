import setuptools
with open("README.md", "r", encoding="utf-8") as fl:
    long_description = fl.read()

setuptools.setup(
    name='Aboutn',
    version='0.2.2.10',
    url='https://github.com/AkiraDemenech/About-n-Squares/',
    license='MIT License',
    author= 'Guilherme Akira Demenech Mori',
    author_email='akira.demenech@gmail.com',
    keywords='art constructivism game',
    description='An Art and Genetic Algorithms Exploration Package based on Russian Constructivism bidimensional graphic works, ideas and method; ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent",],
)