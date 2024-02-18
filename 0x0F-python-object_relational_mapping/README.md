# Python - Object-relational mapping

## Overview

This project involves integrating two worlds: databases and Python. It consists of two parts:

1. Using the `MySQLdb` module to connect to a MySQL database and execute SQL queries.
2. Utilizing the `SQLAlchemy` module, an Object Relational Mapper (ORM), to abstract the storage to usage, thereby eliminating the need to write SQL queries directly.

With an ORM, the primary focus shifts from understanding how an object is stored to what can be done with the objects, making the code independent of the storage type.

## Authored

This project made by [Hicham Bourezi](https://github.com/Dragonkuro2).

## Background Context

In the first part of the project, MySQLdb module is employed to connect to a MySQL database and execute SQL queries. The second part uses SQLAlchemy, which simplifies database interactions by providing a Pythonic interface.

## Resources

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/user_guide.html)
- [MySQLdb tutorial](https://www.tutorialspoint.com/python3/python_database_access.htm)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/index.html)
- [Introduction to SQLAlchemy](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.x/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## Learning Objectives

Upon completion of this project, learners should be able to:

- Explain the benefits of Python programming.
- Connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations on MySQL tables using Python.
- Define ORM and map Python classes to MySQL tables.
- Create a Python Virtual Environment for project-specific dependencies.

## Requirements

- Allowed editors: vi, vim, emacs
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files should be executed with MySQLdb version 2.0.x and SQLAlchemy version 1.4.x
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should adhere to pycodestyle (version 2.8.*)
- All files must be executable
- File length will be tested using wc
- Modules, classes, and functions must have documentation

## Installation Instructions

### Python Virtual Environment

To create a Python Virtual Environment for this project, follow these steps:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

**MySQLdb Module**

To install MySQLdb module version 2.0.x, execute the following commands:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```
