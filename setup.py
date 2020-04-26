# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="django-ace",
    version="1.1.0rc1",
    description="django-ace provides integration for ajax.org ACE with Django",
    long_description=open("README.rst").read(),
    author="Bradley Ayers",
    author_email="bradley.ayers@gmail.com",
    license="Simplified BSD",
    url="https://github.com/django-ace/django-ace",
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    install_requires=["Django>1.11"],
    tests_require=["html5lib"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
)
