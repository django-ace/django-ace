from setuptools import setup, find_packages


setup(
    name='django-ace',
    version="0.1.0",
    description='django-ace provides integration for ajax.org ACE with Django',
    long_description=open('README.rst').read(),

    author='Bradley Ayers',
    author_email='bradley.ayers@gmail.com',
    license="BSD",
    url='https://github.com/bradleyayers/django-ace',

    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    install_requires=['Django'],

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
