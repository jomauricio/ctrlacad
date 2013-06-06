.. 

ctrlacad
======================

Quickstart
----------

To bootstrap the project::

    virtualenv ctrlacad
    source ctrlacad/bin/activate
    cd path/to/ctrlacad/repository
    pip install -r requirements.pip
    pip install -e .
    cp ctrlacad/settings/local.py.example ctrlacad/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
