r"""Contains a function that determines the fully-qualified class name of a 
given object or class.

"""



#####################################
## Load libraries/packages/modules ##
#####################################



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2024"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["fully_qualified_class_name"]



def fully_qualified_class_name(obj_or_cls):
    r"""Get fully qualified class name of given input object or class.

    Parameters
    ----------
    obj_or_cls : any type
        Input object or class.

    Returns
    -------
    result : `str`
        The fully qualified class name of ``obj_or_cls``.

    """
    if isinstance(obj_or_cls, type):
        cls = obj_or_cls
    else:
        obj = obj_or_cls
        cls = obj.__class__

    module = cls.__module__

    if module == "builtins":
        result = cls.__qualname__
    else:
        result = module + "." + cls.__qualname__
    
    return result



###########################
## Define error messages ##
###########################
