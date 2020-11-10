Bump Ace version
================

Just run ``sh bin/upgrade_ace.sh``.


How to release
==============

- Update the Changelog.
- Update version in :file:`setup.py` and :file:`django_ace/__init__.py`.
- Commit with a message like "Bump to version 1.0.9".
- Tag it, with the ``v`` prefix, like ``git tag v1.0.9``.
- Test it one last time.
- Ensure you have ``setuptools``, ``wheel``, and ``twine`` up to date.
- Build: ``python setup.py sdist bdist_wheel``.
- Push to pypi: ``twine upload dist/*``.
