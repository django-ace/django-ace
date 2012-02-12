from setuptools import setup, find_packages

setup(
    name='django-ace-editor',
    version="1.0.0",
    description='django-ace-editor is an implementation of the ajax.org Ace editor as a form control.',
    long_description=open('README.md').read(),
    author='Kit Sunde',
    author_email='kitsunde@gmail.com',
    url='https://github.com/Celc/django-ace-editor',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    keywords="editor forms widget",
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