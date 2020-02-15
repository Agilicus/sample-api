"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

exec(compile(open('api/version.py', "rb").read(),
     'api/version.py', 'exec'))

setup(
    name='api',

    version=__version__,  # noqa: F821

    description='Sample API',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/Agilicus/sample-api',

    author='Agilicus',

    author_email='dev@agilicus.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='OpenAPI',

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'tools']),

    python_requires='>=3.7, <4',

    install_requires=['Flask', 'connexion'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={},

    data_files=[],

    entry_points={},

    project_urls={},
)
