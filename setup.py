"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open
import os
import inspect

readme_dir = os.path.dirname(os.path.realpath(os.path.abspath(inspect.getfile(inspect.currentframe()))))
readme = 'README.md'

with open(os.path.join(readme_dir, readme)) as long_description:
	long_description = long_description.read()

setup(
    name='cloudroutes_common_pkg',

    description='Common Files to Runbook Containers',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/asm-products/cloudroutes-service',

    license='AGPL',

    classifiers=[
        #   3 - Alpha
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: GNU AGPL License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='IT automation self-healing devops reactions monitors',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
	setup_requires = ['pyyaml', 'rethinkdb', 'guppy', 'django', 'gevent', 'requests[security]'],
    install_requires=['pyyaml', 'rethinkdb', 'guppy', 'django', 'gevent'],
)
