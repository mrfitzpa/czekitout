.. _installation_instructions_sec:

Installation instructions
=========================

First, open up the appropriate command line interface. On Unix-based systems,
you would open a terminal. On Windows systems you would open an Anaconda Prompt
as an administrator.

Next, assuming that you have downloaded/cloned the ``czekitout`` git repository,
change into the root of said repository, and run the following command::

  pip install .

Note that you must include the period as well. This will install ``czekitout``
along with all of its dependencies, namely ``numpy`` and ``pytest``.

Update czekitout
----------------

If you, or someone else has made changes to this library, you can reinstall it
by issuing the following command::
  
    pip install .

Uninstall czekitout
-------------------

To uninstall ``czekitout``, all you need to type is::

  pip uninstall czekitout

Generating documention files
----------------------------

To generate documentation in html format from source files, you will also need
to install several other packages. This can be done by running the following
command from the root of the repository::

  pip install -r requirements-doc.txt

Next, assuming that you are in the root of the repository, that you have
installed all the prerequisite packages, and that ``czekitout`` has been
installed, you can generate the ``czekitout`` documentation html files by
issuing the following commands within your virtual environment::

  cd docs
  make html

This will generate a set of html files in ``./_build/html`` containing the
documentation of ``czekitout``. You can then open any of the files using your
favorite web browser.

If ``czekitout`` has been updated, the documentation has most likely changed as
well. To update the documentation simply run::

  make html

again to generate the new documentation.
