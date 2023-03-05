Bump Ace version
================

Just run ``sh bin/upgrade_ace.sh``.


How to release
==============

- Update the Changelog in :file:`README.rst`.
- Update version in :file:`django_ace/__init__.py`.
- Commit with a message like "Update ACE to 1.14.0".
- Tag it, with the ``v`` prefix, like ``git tag v1.0.9``.
- Test it one last time.
- git push && git push --tags
- Ensure you have ``build``, and ``twine`` up to date.
- Build: ``python -m build``.
- Push to pypi: ``twine upload dist/*``.
- Create realease from the tag on Github
