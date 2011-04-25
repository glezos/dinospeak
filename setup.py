from distutils.core import setup, Extension

readme_file = open(u'README')
long_description = readme_file.read()

setup(
    name = "dinospeak",
    description = ("Dinosaur language translation library"),
    long_description = long_description,
    version = "0.1",
    author = 'Dimitris Glezos',
    author_email = 'glezos@indifex.com',
    zip_safe = False,
    )
