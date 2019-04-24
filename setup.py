import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='tda-utilities',
    version='0.1',
    author='Benedict Aquino',
    author_email='benaq9@gmail.com',
    description='Computational Topology Utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/benedictaquino/tda-numbers/',
    packages=setuptools.find_packages()
)
