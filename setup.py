from os.path import join
import re
from setuptools import setup, find_packages


# dynamically pull the version from django_ace/__init__.py
version = re.search('^__version__ = "(.+?)"$',
                    open(join('django_ace', '__init__.py')).read(), re.MULTILINE).group(1)

setup(
    name='django-ace',
    version=version,
    description='django-ace provides integration for ajax.org ACE with Django',
    long_description=open('README.rst').read(),

    author='Bradley Ayers',
    author_email='bradley.ayers@gmail.com',
    license="Simplified BSD",
    url='https://github.com/bradleyayers/django-ace',

    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    install_requires=['Django>1.11'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
    )
