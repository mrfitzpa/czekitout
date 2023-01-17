.. _installation_instructions_sec:

Installation instructions
=========================

Install czekitout
-----------------

First, open up the appropriate command line interface. On Unix-based systems,
you would open a terminal. On Windows systems you would open an Anaconda Prompt
as an administrator.

Next, assuming that you have downloaded/cloned the ``czekitout`` git repository,
change into the root of said repository, and run the following command::

  pip install .

Note that you must include the period as well. The above command executes a
standard installation of ``czekitout``. Upon completing the standard
installation of ``czekitout``, a set of libraries should be installed including
``numpy``, and ``pytest``.

Optionally, for additional features in ``czekitout``, one can install additional
dependencies upon installing ``czekitout``. To install a subset of additional
dependencies, run the following command from the root of the repository::

  pip install .[<selector>]

where ``<selector>`` can be one of the following::

  - ``doc``: to install the dependencies necessary for documentation generation;
  - ``all``: to install all additional dependencies, which is simply all the
    dependencies necessary for documentation generation.

Update czekitout
----------------

If you, or someone else has made changes to this library, you can reinstall it
by issuing the following command::
  
    pip install .

or the command::

  pip install .[<selector>]

where ``<selector>`` was described in the previous section.

Uninstall czekitout
-------------------

To uninstall ``czekitout``, run the following command from the root of the
repository::

  pip uninstall czekitout

Generating documention files
----------------------------

To generate documentation in html format from source files, you will also need
to install several other packages. This can be done by running the following
command from the root of the repository::

  pip install .[doc]

or the command::

  pip install .[all]

Note that the latter command will install all extra dependencies of
``czekitout``.

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
