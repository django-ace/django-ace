from setuptools import setup, find_packages

setup(
    name="django-ace",
    version="1.0.7",
    description="django-ace provides integration for ajax.org ACE with Django",
    long_description=open("README.rst").read(),
    author="Bradley Ayers",
    author_email="bradley.ayers@gmail.com",
    license="Simplified BSD",
    url="https://github.com/django-ace/django-ace",
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    install_requires=["Django>1.11"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
