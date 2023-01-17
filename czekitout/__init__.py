"""``czekitout`` is a Python library that contains a collection of functions
that facilitate type-checking, validation, and type-conversions, with useful
error messages when exceptions are thrown.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import child modules and packages of current package.
import czekitout.name
import czekitout.isa
import czekitout.check
import czekitout.convert
import czekitout.version



############################
## Authorship information ##
############################

__author__       = "Matthew Fitzpatrick"
__copyright__    = "Copyright 2023"
__credits__      = ["Matthew Fitzpatrick"]
__version__      = czekitout.version.version
__full_version__ = czekitout.version.full_version
__maintainer__   = "Matthew Fitzpatrick"
__email__        = "mrfitzpa@uvic.ca"
__status__       = "Development"



###################################
## Useful background information ##
###################################

# See e.g. ``https://docs.python.org/3/reference/import.html#regular-packages``
# for a brief discussion of ``__init__.py`` files.



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["show_config"]



def show_config():
    """Print information about the version of ``czekitout`` and libraries it 
    uses.

    """
    print(version.version_summary)

    return None



###########################
## Define error messages ##
###########################
