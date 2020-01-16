import io
import os
import sys

import setuptools


def get_version_from_package() -> str:
    path = os.path.join(os.path.dirname(__file__), "__init__.py")
    path = os.path.normpath(os.path.abspath(path))
    with open(path) as f:
        for line in f:
            if line.startswith("__version__"):
                version = line.split(" = ", 1)
                version = version.replace("'", "").strip()
                return version

name = "pakkaransdb"
desc = "Pakkarans assistant"


classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: Freely Distributable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation',
    'Programming Language :: Python :: Implementation :: CPython'
]
author = 'pocoyo'
author_email = 'pocoyo@thomasvijay'
license = 'Apache License Version 2.0'
packages = [
    'helpers',
    'test'
]

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_params = dict(
    name=name,
    version=get_version_from_package(),
    description=desc,
    long_description=desc,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    author=author,
    author_email=author_email,
    license=license,
    packages=packages,
    include_package_data=True,
    install_requires=install_require,
    setup_requires=pytest_runner,
    python_requires='>=3.5.*'
)


def main():
    """Package installation entry point."""
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()

