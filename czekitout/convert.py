r"""Contains functions that facilitate type-conversions with useful error
messages when exceptions are thrown.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For performing deep copies.
import copy



# For general array handling.
import numpy as np



# For type-checking objects.
import czekitout.isa

# For validating objects.
import czekitout.check



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
__all__ = ["to_dict",
           "to_str_from_str_like",
           "to_str_from_path_like",
           "to_multi_dim_slice",
           "to_list_of_ints",
           "to_tuple_of_ints",
           "to_pair_of_floats",
           "to_pair_of_positive_floats",
           "to_pair_of_positive_ints",
           "to_pair_of_nonnegative_ints",
           "to_real_two_column_numpy_matrix",
           "to_bool",
           "to_float",
           "to_int",
           "to_positive_float",
           "to_nonnegative_float",
           "to_positive_int",
           "to_numpy_array",
           "to_real_numpy_matrix",
           "to_real_numpy_array_3d",
           "to_bool_numpy_matrix",
           "to_bool_numpy_array_3d"]



def to_dict(obj, obj_name):
    r"""Convert input object to an instance of the class `dict`.

    If the input object is not dictionary-like, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be dictionary-like.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if isinstance(obj, dict):
        result = obj
    else:
        czekitout.check.if_dict_like(obj, obj_name)
        result = dict(obj)

    return result



def to_str_from_str_like(obj, obj_name):
    r"""Convert string-like input object to an instance of the class `str`.

    If the input object is not string-like, then a `TypeError` is raised with
    the message::

        The object ``<obj_name>`` must be an instance of the class `str`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `str`
        The object resulting from the conversion.

    """
    if isinstance(obj, str):
        result = obj
    else:
        czekitout.check.if_str_like(obj, obj_name)
        result = str(obj)

    return result



def to_str_from_path_like(obj, obj_name):
    r"""Convert path-like input object to an instance of the class `str`.

    If the input object is not path-like, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be an instance of the class `str`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `str`
        The object resulting from the conversion.

    """
    czekitout.check.if_path_like(obj, obj_name)
    result = str(obj)

    return result



def to_multi_dim_slice(obj, obj_name):
    r"""Convert a multi-dimensional slice-like input object to a 
    multi-dimensional slice object.

    We define a multi-dimensional slice-like object as a sequence of items which
    contains at most one item being a sequence of integers, and the remaining
    items being `slice` objects and/or integers.

    We define a multi-dimensional slice object as a `tuple` of items which
    contains at most one item being a `list` of integers, and the remaining
    items being `slice` and/or `int` objects.

    If the input object is not multi-dimensional slice-like, then a `TypeError`
    is raised with the message::

        The object ``<obj_name>`` must be a sequence of items which contains at 
        most one item being a sequence of integers, and the remaining items 
        being `slice` objects and/or integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `str`
        The object resulting from the conversion.

    """
    czekitout.check.if_multi_dim_slice_like(obj, obj_name)
    result = list(obj)

    for idx_1, single_dim_slice in enumerate(obj):
        if isinstance(single_dim_slice, slice):
            result[idx_1] = copy.deepcopy(single_dim_slice)
            continue

        try:
            result[idx_1] = [0]*len(single_dim_slice)
            for idx_2, num in enumerate(single_dim_slice):
                result[idx_1][idx_2] = int(num)
            continue
        except:
            pass

        result[idx_1] = int(obj[idx_1])

    result = tuple(result)
    
    return result



def to_list_of_ints(obj, obj_name):
    r"""Convert input object to a list of `ints`.

    If the input object is not a sequence of integers, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a sequence of integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_int_seq(obj, obj_name)
    result = list(int(num) for num in obj)

    return result



def to_tuple_of_ints(obj, obj_name):
    r"""Convert input object to a tuple of `int` objects.

    If the input object is not a sequence of integers, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a sequence of integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_int_seq(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_pair_of_floats(obj, obj_name):
    r"""Convert input object to a two-element tuple of `float` objects.

    If the input object is not a pair of real numbers, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a pair of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_pair_of_floats(obj, obj_name)
    result = tuple(float(num) for num in obj)

    return result



def to_pair_of_positive_floats(obj, obj_name):
    r"""Convert input object to a two-element tuple of positive `float` objects.

    If the input object is not a pair of positive real numbers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of positive real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_pair_of_positive_floats(obj, obj_name)
    result = tuple(float(num) for num in obj)

    return result



def to_pair_of_positive_ints(obj, obj_name):
    r"""Convert input object to a two-element tuple of positive `int` objects.

    If the input object is not a pair of positive integers, then a `TypeError`
    is raised with the message::

        The object ``<obj_name>`` must be a pair of positive integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_pair_of_positive_ints(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_pair_of_nonnegative_ints(obj, obj_name):
    r"""Convert input object to a two-element tuple of non-negative `int` 
    objects.

    If the input object is not a pair of non-negative integers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of non-negative integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_pair_of_nonnegative_ints(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_real_two_column_numpy_matrix(obj, obj_name):
    r"""Convert input object to a real-valued 2D two-column numpy array.

    If the input object is not a real-valued two-column matrix, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a be a two-column matrix of real 
        numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    err_msg = _to_real_two_column_numpy_matrix_err_msg_1.format(obj_name)
    
    if czekitout.isa.real_two_column_numpy_matrix(obj):
        result = obj
    else:
        try:
            result = np.array(obj, dtype=float)
        except:
            raise TypeError(err_msg)
        czekitout.check.if_real_two_column_numpy_matrix(result, obj_name)

    return result



def to_bool(obj, obj_name):
    r"""Convert input object to a `bool`.

    If the input object is not a boolean, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be an instance of the class `bool`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_bool(obj, obj_name)
    result = bool(int(obj))

    return result



def to_float(obj, obj_name):
    r"""Convert input object to a `float`.

    If the input object is not a floating-point number, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be an instance of the class `float`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_float(obj, obj_name)
    result = float(obj)

    return result



def to_int(obj, obj_name):
    r"""Convert input object to a `int`.

    If the input object is not an integer, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be an instance of the class `int`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_int(obj, obj_name)
    result = int(obj)

    return result



def to_positive_float(obj, obj_name):
    r"""Convert input object to a positive `float`.

    If the input object is not a positive floating-point number, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a positive `float`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_positive_float(obj, obj_name)
    result = float(obj)

    return result



def to_nonnegative_float(obj, obj_name):
    r"""Convert input object to a nonnegative `float`.

    If the input object is not a nonnegative floating-point number, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a nonnegative `float`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_nonnegative_float(obj, obj_name)
    result = float(obj)

    return result



def to_nonnegative_int(obj, obj_name):
    r"""Convert input object to a nonnegative `int`.

    If the input object is not a nonnegative integer, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a nonnegative `int`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_nonnegative_int(obj, obj_name)
    result = int(obj)

    return result



def to_positive_int(obj, obj_name):
    r"""Convert input object to a positive `int`.

    If the input object is not a positive integer, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be a positive `int`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    czekitout.check.if_positive_int(obj, obj_name)
    result = int(obj)

    return result



def to_numpy_array(obj, obj_name):
    r"""Convert input object to a numpy array.

    If the input object is not an array, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be an array.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if czekitout.isa.numpy_array(obj):
        result = obj
    else:
        try:
            result = np.array(obj)
        except:
            err_msg = _to_numpy_array_err_msg_1.format(obj_name)
            raise TypeError(err_msg)

    return result



def to_real_numpy_matrix(obj, obj_name):
    r"""Convert input object to a real-valued numpy array.

    If the input object is not a real-valued matrix, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be real-valued matrix.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if czekitout.isa.real_numpy_matrix(obj):
        result = obj
    else:
        try:
            result = np.array(obj, dtype=float)
        except:
            err_msg = _to_real_numpy_matrix_err_msg_1.format(obj_name)
            raise TypeError(err_msg)

    return result



def to_real_numpy_array_3d(obj, obj_name):
    r"""Convert input object to a real-valued 3D numpy array.

    If the input object is not a real-valued 3D matrix, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be real-valued 3D matrix.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if czekitout.isa.real_numpy_array_3d(obj):
        result = obj
    else:
        try:
            result = np.array(obj, dtype=float)
        except:
            err_msg = _to_real_numpy_array_3d_err_msg_1.format(obj_name)
            raise TypeError(err_msg)
        czekitout.check.if_real_numpy_array_3d(result, obj_name)

    return result



def to_bool_numpy_matrix(obj, obj_name):
    r"""Convert input object to a boolean 2D numpy array.

    If the input object is not a boolean 2D matrix, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be boolean matrix.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if czekitout.isa.bool_numpy_matrix(obj):
        result = obj
    else:
        czekitout.check.if_bool_matrix(obj, obj_name)
        result = np.array(obj, dtype=bool)

    return result



def to_bool_numpy_array_3d(obj, obj_name):
    r"""Convert input object to a boolean 3D numpy array.

    If the input object is not a boolean 3D matrix, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be 3D boolean matrix.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    Returns
    -------
    result : `dict`
        The object resulting from the conversion.

    """
    if czekitout.isa.bool_numpy_array_3d(obj):
        result = obj
    else:
        czekitout.check.if_bool_array_3d(obj, obj_name)
        result = np.array(obj, dtype=bool)

    return result



###########################
## Define error messages ##
###########################

_to_real_two_column_numpy_matrix_err_msg_1 = \
    ("The object ``{}`` must be two-column matrix of real numbers.")

_to_numpy_array_err_msg_1 = \
    ("The object ``{}`` must be an array.")

_to_real_numpy_matrix_err_msg_1 = \
    ("The object ``{}`` must be a real-valued matrix.")

_to_real_numpy_array_3d_err_msg_1 = \
    ("The object ``{}`` must be a real-valued 3D array.")

