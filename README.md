simpledb
========

Simple wrapper around SQLalchemy

This module hides the complexity of SQLAlchemy to provide a simple interface to
store and manipulate Python objects each with a set of properties. Unlike the
default behaviour of sqlalchemy's declaritive_base, inheritance of objects will
not require "join", rather it creates a separate table. This makes it easy to
use objects around from parts of not-so-related applications.

For example, a ``SourcePackage`` table is created by Grail. Then, PyPM will
extend it as ``BinaryPackage`` which gets extended to ``RepoPackage``. The table
for RepoPackage will be concretely inherited, meaning - there will be just be
one table without having to 'join' to another SourcePackage table.

At the moment, PyPM and Grail use this module. It may not be of use to others,
and we may change the api/behaviour. Hence, it makes sense to keep it as an
internal module.
