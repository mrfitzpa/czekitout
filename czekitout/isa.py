r"""Contains functions that facilitate type-checking.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For general array handling.
import numpy as np



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2022"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["numpy_array",
           "real_numpy_array",
           "bool_numpy_array",
           "numpy_matrix",
           "two_column_numpy_matrix",
           "real_numpy_matrix",
           "numpy_array_3d",
           "real_numpy_array_3d",
           "real_two_column_numpy_matrix",
           "bool_numpy_matrix",
           "bool_numpy_array_3d"]



def numpy_array(obj):
    r"""Returns ``True`` if input object is a numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a numpy array, otherwise it
        is set to ``False``.

    """
    result = isinstance(obj, np.ndarray)

    return result



def real_numpy_array(obj):
    r"""Returns ``True`` if input object is a real-valued numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a real-valued numpy array, 
        otherwise it is set to ``False``.

    """
    is_numpy_array = numpy_array  # Alias for readability.
    
    if is_numpy_array(obj):
        result = np.isrealobj(obj)
    else:
        result = False

    return result



def bool_numpy_array(obj):
    r"""Returns ``True`` if input object is a boolean numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a boolean numpy array,
        otherwise it is set to ``False``.

    """
    is_numpy_array = numpy_array  # Alias for readability.
    
    if is_numpy_array(obj):
        result = (obj.dtype == bool)
    else:
        result = False

    return result



def numpy_matrix(obj):
    r"""Returns ``True`` if input object is a 2D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a 2D numpy array, otherwise 
        it is set to ``False``.

    """
    is_numpy_array = numpy_array  # Alias for readability.

    if is_numpy_array(obj):
        result = (len(obj.shape) == 2)
    else:
        result = False

    return result



def two_column_numpy_matrix(obj):
    r"""Returns ``True`` if input object is a 2D two-column numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a 2D two-column numpy array,
        otherwise it is set to ``False``.

    """
    is_numpy_matrix = numpy_matrix  # Alias for readability.

    if is_numpy_matrix(obj):
        result = (obj.shape[1] == 2)
    else:
        result = False

    return result



def real_numpy_matrix(obj):
    r"""Returns ``True`` if input object is a real-valued 2D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a real-valued 2D numpy 
        array, otherwise it is set to ``False``.

    """
    is_numpy_matrix = numpy_matrix  # Alias for readability.
    is_real_numpy_array = real_numpy_array  # Alias for readability.

    result = (is_numpy_matrix(obj) and is_real_numpy_array(obj))

    return result



def numpy_array_3d(obj):
    r"""Returns ``True`` if input object is a 3D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a 3D numpy array, otherwise 
        it is set to ``False``.

    """
    is_numpy_array = numpy_array  # Alias for readability.

    if is_numpy_array(obj):
        result = (len(obj.shape) == 3)
    else:
        result = False

    return result



def real_numpy_array_3d(obj):
    r"""Returns ``True`` if input object is a real-valued 3D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a real-valued 3D numpy 
        array, otherwise it is set to ``False``.

    """
    is_numpy_array_3d = numpy_array_3d  # Alias for readability.
    is_real_numpy_array = real_numpy_array  # Alias for readability.

    result = (is_numpy_array_3d(obj) and is_real_numpy_array(obj))

    return result



def real_two_column_numpy_matrix(obj):
    r"""Returns ``True`` if input object is a real-valued 2D two-column numpy 
    array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a real-valued 2D two-column 
        numpy array, otherwise it is set to ``False``.

    """
    # Aliases for readability.
    is_two_column_numpy_matrix = two_column_numpy_matrix
    is_real_numpy_array = real_numpy_array

    result = (is_two_column_numpy_matrix(obj) and is_real_numpy_array(obj))

    return result



def bool_numpy_matrix(obj):
    r"""Returns ``True`` if input object is a boolean 2D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a bolean 2D numpy array, 
        otherwise it is set to ``False``.

    """
    is_numpy_matrix = numpy_matrix  # Alias for readability.
    is_bool_numpy_array = bool_numpy_array  # Alias for readability.

    result = (is_numpy_matrix(obj) and is_bool_numpy_array(obj))

    return result



def bool_numpy_array_3d(obj):
    r"""Returns ``True`` if input object is a boolean 3D numpy array.

    Parameters
    ----------
    obj : any type
        Input object.

    Returns
    -------
    result : `bool`
        ``result`` is set to ``True`` if ``obj`` is a boolean 3D numpy array, 
        otherwise it is set to ``False``.

    """
    is_numpy_array_3d = numpy_array_3d  # Alias for readability.
    is_bool_numpy_array = bool_numpy_array  # Alias for readability.

    result = (is_numpy_array_3d(obj) and is_bool_numpy_array(obj))

    return result



###########################
## Define error messages ##
###########################
