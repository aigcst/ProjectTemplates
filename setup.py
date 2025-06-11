from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
PATCH = 1
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"


def get_install_requires():
    reqs = []
    return reqs


setup(
    name="xx",
    version=VERSION,
    author="aigcst",
    author_email="aigcst@outlook.com",
    long_description_content_type="text/markdown",
    url='https://github.com/aigcst/xx.git',
    long_description=open('README.md', encoding="utf-8").read(),
    python_requires=">=3.8",
    install_requires=get_install_requires(),
    packages=find_packages(),
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_data={'': ['*.csv', '*.txt', '.toml']},
    include_package_data=True,
)
