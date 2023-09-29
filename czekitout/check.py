r"""Contains functions that facilitate validation with useful error messages 
when exceptions are thrown.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# To determine whether an object is path-like.
import os.path



# For general array handling.
import numpy as np



# For getting fully qualified class names.
import czekitout.name

# For type-checking objects.
import czekitout.isa



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2023"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["if_instance_of_any_accepted_types",
           "if_dict_like",
           "if_str_like",
           "if_str_like_seq",
           "if_one_of_any_accepted_strings",
           "if_path_like",
           "if_path_like_seq",
           "if_int",
           "if_int_seq",
           "if_positive_int",
           "if_positive_int_seq",
           "if_nonnegative_int",
           "if_nonnegative_int_seq",
           "if_multi_dim_slice_like",
           "if_float",
           "if_float_seq",
           "if_positive_float",
           "if_positive_float_seq",
           "if_nonnegative_float",
           "if_nonnegative_float_seq",
           "if_pair_of_floats",
           "if_pair_of_positive_floats",
           "if_pair_of_nonnegative_floats",
           "if_pair_of_ints",
           "if_pair_of_positive_ints",
           "if_pair_of_nonnegative_ints",
           "if_quadruplet_of_nonnegative_ints",
           "if_pairs_of_floats",
           "if_real_numpy_array",
           "if_real_numpy_array_1d",
           "if_real_numpy_matrix",
           "if_real_two_column_numpy_matrix",
           "if_real_numpy_array_3d",
           "if_nonnegative_numpy_array",
           "if_nonnegative_numpy_matrix",
           "if_bool",
           "if_bool_matrix",
           "if_bool_array_3d",
           "if_callable"]



def if_instance_of_any_accepted_types(obj, obj_name, accepted_types):
    r"""Check whether input object is one of any given accepted types.

    If the input object is not one of any given accepted type, and 
    ``len(accepted_types)=1``, then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be instance of the class 
        `<accepted_type>`.

    where <obj_name> is replaced by the contents of the string ``obj_name``, and
    <accepted_type> by the fully qualified class name of ``accepted_types[0]``.

    If the input object is not one of any given accepted type, and 
    ``len(accepted_types)>1``, then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be instance of one of the following 
        classes: <accepted_types>.

    where <obj_name> is replaced by the contents of the string ``obj_name``, and
    <accepted_types>  by the sequence of the fully qualified class names of the
    accepted types stored in ``accepted_types``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.
    accepted_types : `array_like` (`type`, ndim=1)
        Accepted types.

    """
    if not isinstance(obj, accepted_types):
        fully_qualified_class_name = \
            czekitout.name.fully_qualified_class_name # Alias for readability.
        names_of_accepted_types = \
            tuple(fully_qualified_class_name(accepted_type)
                  for accepted_type in accepted_types)
                
        if len(names_of_accepted_types) == 1:
            err_msg = _if_instance_of_any_accepted_types_err_msg_1
            err_msg = err_msg.format(obj_name, names_of_accepted_types[0])
        else:
            names_of_accepted_types = \
                str(names_of_accepted_types).replace("\'", "`")
            err_msg = _if_instance_of_any_accepted_types_err_msg_2
            err_msg = err_msg.format(obj_name, names_of_accepted_types)
            
        raise TypeError(err_msg)

    return None



def if_dict_like(obj, obj_name):
    r"""Check whether input object is dictionary-like.

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

    """
    try:
        dict(obj)
    except:
        err_msg = _if_dict_like_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_str_like(obj, obj_name):
    r"""Check whether input object is string-like.

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

    """
    check_if_instance_of_any_accepted_types = \
        if_instance_of_any_accepted_types  # Alias for readability.

    accepted_types = (str, bytes)
    check_if_instance_of_any_accepted_types(obj, obj_name, accepted_types)

    return None



def if_str_like_seq(obj, obj_name):
    r"""Check whether input object is a sequence of string-like objects.

    If the input object is not a sequence of string-like objects, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of strings.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for str_like_obj in obj:
            check_if_str_like = if_str_like  # Alias for readability.
            check_if_str_like(str_like_obj, "str_like_obj")
    except:
        err_msg = _if_str_like_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_one_of_any_accepted_strings(obj, obj_name, accepted_strings):
    r"""Check whether input object is one of any given accepted strings.

    If the input object is not one of any given accepted string, and 
    ``len(accepted_strings)=1``, then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be set to ``<accepted_string>``.

    where <obj_name> is replaced by the contents of the string ``obj_name``, and
    <accepted_string> by the accepted string.

    If the input object is not one of any given accepted string, and 
    ``len(accepted_strings)>1``, then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be set to one of the following strings: 
        ``<accepted_strings>``.

    where <obj_name> is replaced by the contents of the string ``obj_name``, and
    <accepted_strings> by the sequence of strings stored in
    ``accepted_strings``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.
    accepted_strings : `array_like` (`str`, ndim=1)
        Accepted strings.

    """
    if obj not in accepted_strings:
        if len(accepted_strings) == 1:
            err_msg = _if_one_of_any_accepted_strings_err_msg_1
            err_msg = err_msg.format(obj_name, accepted_strings[0])
        else:
            err_msg = _if_one_of_any_accepted_strings_err_msg_2
            err_msg = err_msg.format(obj_name, str(accepted_strings))
            
        raise TypeError(err_msg)

    return None



def if_path_like(obj, obj_name):
    r"""Check whether input object is path-like.

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

    """
    try:
        os.path.exists(obj)
    except:
        err_msg = _if_instance_of_any_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "str")
        raise TypeError(err_msg)

    return None



def if_path_like_seq(obj, obj_name):
    r"""Check whether input object is a sequence of path-like objects.

    If the input object is not a sequence of path-like objects, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of strings.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for path_like_obj in obj:
            check_if_path_like = if_path_like  # Alias for readability.
            check_if_path_like(path_like_obj, "path_like_obj")
    except:
        err_msg = _if_path_like_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_int(obj, obj_name):
    r"""Check whether input object is an integer.

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

    """
    try:
        if abs(int(obj) - obj) > 1.0e-14:
            raise
    except:
        err_msg = _if_instance_of_any_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "int")
        raise TypeError(err_msg)

    return None



def if_int_seq(obj, obj_name):
    r"""Check whether input object is a sequence of integers.

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

    """
    try:
        for num in obj:
            check_if_int = if_int  # Alias for readability.
            check_if_int(num, "num")
    except:
        err_msg = _if_int_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_positive_int(obj, obj_name):
    r"""Check whether input object is a positive integer.

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

    """
    check_if_int = if_int  # Alias for readability.
    check_if_int(obj, obj_name)
    
    try:
        if int(obj) < 1:
            raise
    except:
        err_msg = _if_positive_int_err_msg_1.format(obj_name)
        raise ValueError(err_msg)

    return None



def if_positive_int_seq(obj, obj_name):
    r"""Check whether input object is a sequence of positive integers.

    If the input object is not a sequence of positive integers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of positive integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for num in obj:
            check_if_positive_int = if_positive_int  # Alias for readability.
            check_if_positive_int(num, "num")
    except:
        err_msg = _if_positive_int_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_nonnegative_int(obj, obj_name):
    r"""Check whether input object is a nonnegative integer.

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

    """
    check_if_int = if_int  # Alias for readability.
    check_if_int(obj, obj_name)
    
    try:
        if int(obj) < 0:
            raise
    except:
        err_msg = _if_nonnegative_int_err_msg_1.format(obj_name)
        raise ValueError(err_msg)

    return None



def if_nonnegative_int_seq(obj, obj_name):
    r"""Check whether input object is a sequence of nonnegative integers.

    If the input object is not a sequence of nonnegative integers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of nonnegative integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for num in obj:
            # Alias for readability.
            check_if_nonnegative_int = if_nonnegative_int
            
            check_if_nonnegative_int(num, "num")
    except:
        err_msg = _if_nonnegative_int_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_multi_dim_slice_like(obj, obj_name):
    r"""Check whether input object is a multi-dimensional slice-like object.

    We define a multi-dimensional slice-like object as a sequence of items which
    contains at most one item being a sequence of integers, and the remaining
    items being `slice` objects and/or integers.

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

    """
    num_single_dim_slices_as_lists = 0
    
    try:
        for single_dim_slice in obj:
            if isinstance(single_dim_slice, slice):
                continue

            check_if_int = if_int  # Alias for readability.
            
            try:
                for num in single_dim_slice:
                    check_if_int(num, "num")
                num_single_dim_slices_as_lists += 1
                continue
            except:
                pass

            check_if_int(single_dim_slice, "single_dim_slice")

        if num_single_dim_slices_as_lists > 1:
            raise

    except:
        err_msg = _if_multi_dim_slice_like_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_float(obj, obj_name):
    r"""Check whether input object is a floating-point number.

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

    """
    try:
        if abs(float(obj) - obj) > 1.0e-14:
            raise
    except:
        err_msg = _if_instance_of_any_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "float")
        raise TypeError(err_msg)

    return None



def if_float_seq(obj, obj_name):
    r"""Check whether input object is a sequence of floating-point numbers.

    If the input object is not a sequence of floating-point numbers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of floating-point numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for num in obj:
            check_if_float = if_float  # Alias for readability.
            check_if_float(num, "num")
    except:
        err_msg = _if_float_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_positive_float(obj, obj_name):
    r"""Check whether input object is a positive floating-point number.

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

    """
    check_if_float = if_float  # Alias for readability.
    check_if_float(obj, obj_name)
    
    if float(obj) <= 0:
        err_msg = _if_positive_float_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_positive_float_seq(obj, obj_name):
    r"""Check whether input object is a sequence of positive floating-point 
    numbers.

    If the input object is not a sequence of positive floating-point numbers,
    then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of positive floating-point
        numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for num in obj:
            check_if_positive_float = \
                if_positive_float  # Alias for readability.
            check_if_positive_float(num, "num")
    except:
        err_msg = _if_positive_float_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_nonnegative_float(obj, obj_name):
    r"""Check whether input object is a nonnegative floating-point number.

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

    """
    check_if_float = if_float  # Alias for readability.
    check_if_float(obj, obj_name)
    
    if float(obj) < 0:
        err_msg = _if_nonnegative_float_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_nonnegative_float_seq(obj, obj_name):
    r"""Check whether input object is a sequence of nonnegative floating-point 
    numbers.

    If the input object is not a sequence of nonnegative floating-point numbers,
    then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of nonnegative
        floating-point numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for num in obj:
            check_if_nonnegative_float = \
                if_nonnegative_float  # Alias for readability.
            check_if_nonnegative_float(num, "num")
    except:
        err_msg = _if_nonnegative_float_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_floats(obj, obj_name):
    r"""Check whether input object is a pair of floating-point numbers.

    If the input object is not a pair of floating-point numbers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            check_if_float = if_float  # Alias for readability.
            check_if_float(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_floats_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_positive_floats(obj, obj_name):
    r"""Check whether input object is a pair of positive floating-point numbers.

    If the input object is not a pair of positive floating-point numbers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of positive real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            check_if_positive_float = \
                if_positive_float  # Alias for readability.
            check_if_positive_float(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_positive_floats_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_nonnegative_floats(obj, obj_name):
    r"""Check whether input object is a pair of nonnegative floating-point 
    numbers.

    If the input object is not a pair of nonnegative floating-point numbers,
    then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of nonnegative real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            check_if_nonnegative_float = \
                if_nonnegative_float  # Alias for readability.
            check_if_nonnegative_float(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_nonnegative_floats_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_ints(obj, obj_name):
    r"""Check whether input object is a pair of integers.

    If the input object is not a pair of integers, then a `TypeError` is raised 
    with the message::

        The object ``<obj_name>`` must be a pair of integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            check_if_int = if_int  # Alias for readability.
            check_if_int(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_ints_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_positive_ints(obj, obj_name):
    r"""Check whether input object is a pair of positive integers.

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

    """
    try:
        count = 0
        for num in obj:
            check_if_positive_int = if_positive_int  # Alias for readability.
            check_if_positive_int(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_positive_ints_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_nonnegative_ints(obj, obj_name):
    r"""Check whether input object is a pair of nonnegative integers.

    If the input object is not a pair of nonnegative integers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a pair of nonnegative integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            # Alias for readability.
            check_if_nonnegative_int = if_nonnegative_int
            check_if_nonnegative_int(num, "num")
            count += 1
        if count != 2:
            raise
    except:
        err_msg = _if_pair_of_nonnegative_ints_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_quadruplet_of_nonnegative_ints(obj, obj_name):
    r"""Check whether input object is a quadruplet of nonnegative integers.

    If the input object is not a quadruplet of nonnegative integers, then a
    `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a quadruplet of nonnegative integers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        count = 0
        for num in obj:
            # Alias for readability.
            check_if_nonnegative_int = if_nonnegative_int
            check_if_nonnegative_int(num, "num")
            count += 1
        if count != 4:
            raise
    except:
        err_msg = _if_quadruplet_of_nonnegative_ints_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pairs_of_floats(obj, obj_name):
    r"""Check whether input object is a sequence of pairs of floating-point 
    numbers.

    If the input object is not a sequence of pairs of floating-point numbers,
    then a `TypeError` is raised with the message::

        The object ``<obj_name>`` must be a sequence of pairs of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        for pair in obj:
            # Alias for readability.
            check_if_pair_of_floats = if_pair_of_floats
            
            check_if_pair_of_floats(pair, "pair")
    except:
        err_msg = _if_pairs_of_floats_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_numpy_array(obj, obj_name):
    r"""Check whether input object is a real-valued numpy array.

    If the input object is not a real-valued numpy array, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a numpy array of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.real_numpy_array(obj):
        err_msg = _if_real_numpy_array_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_numpy_array_1d(obj, obj_name):
    r"""Check whether input object is a real-valued 1D numpy array.

    If the input object is not a real-valued 1D numpy array, then a `TypeError`
    is raised with the message::

        The object ``<obj_name>`` must be a 1D numpy array of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.real_numpy_array_1d(obj):
        err_msg = _if_real_numpy_array_1d_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_numpy_matrix(obj, obj_name):
    r"""Check whether input object is a real-valued 2D numpy array.

    If the input object is not a real-valued 2D numpy array, then a `TypeError`
    is raised with the message::

        The object ``<obj_name>`` must be a 2D numpy array of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.real_numpy_matrix(obj):
        err_msg = _if_real_numpy_matrix_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_two_column_numpy_matrix(obj, obj_name):
    r"""Check whether input object is a real-valued 2D two-column numpy array.

    If the input object is not a real-valued 2D two-column numpy array, then a
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

    """
    if not czekitout.isa.real_two_column_numpy_matrix(obj):
        err_msg = _if_real_two_column_numpy_matrix_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_numpy_array_3d(obj, obj_name):
    r"""Check whether input object is a real-valued 3D numpy array.

    If the input object is not a real-valued 3D numpy array, then a `TypeError`
    is raised with the message::

        The object ``<obj_name>`` must be a 3D numpy array of real numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.real_numpy_array_3d(obj):
        err_msg = _if_real_numpy_array_3d_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_nonnegative_numpy_array(obj, obj_name):
    r"""Check whether input object is a nonnegative numpy array.

    If the input object is not a nonnegative numpy array, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a numpy array of nonnegative numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.nonnegative_numpy_array(obj):
        err_msg = _if_nonnegative_numpy_array_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_nonnegative_numpy_matrix(obj, obj_name):
    r"""Check whether input object is a nonnegative numpy matrix.

    If the input object is not a nonnegative numpy matrix, then a `TypeError` is
    raised with the message::

        The object ``<obj_name>`` must be a numpy matrix of nonnegative numbers.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not czekitout.isa.nonnegative_numpy_matrix(obj):
        err_msg = _if_nonnegative_numpy_matrix_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_bool(obj, obj_name):
    r"""Check whether input object is boolean.

    If the input object is not boolean, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be an instance of the class `bool`.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    try:
        if not isinstance(obj, bool):
            check_if_int = if_int  # Alias for readability.
            check_if_int(obj, obj_name)
            if (int(obj) != 0) and (int(obj) != 1):
                raise
    except:
        err_msg = _if_instance_of_any_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "bool")
        raise TypeError(err_msg)

    return None



def if_bool_matrix(obj, obj_name):
    r"""Check whether input object is a 2D boolean array.

    If the input object is not a 2D boolean array, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be a boolean matrix.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    err_msg = _if_bool_matrix_err_msg_1.format(obj_name)

    try:
        for row in obj:
            for elem in row:
                check_if_bool = if_bool  # Alias for readability.
                check_if_bool(elem, "elem")
    except TypeError:
        raise TypeError(err_msg)
    except IndexError:
        raise IndexError(err_msg)
    except ValueError:
        raise ValueError(err_msg)
    except BaseException as err:
        raise err

    return None



def if_bool_array_3d(obj, obj_name):
    r"""Check whether input object is a 3D boolean array.

    If the input object is not a 3D boolean array, then a `TypeError` is raised
    with the message::

        The object ``<obj_name>`` must be a 3D boolean array.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    err_msg = _if_bool_array_3d_err_msg_1.format(obj_name)

    try:
        for matrix in obj:
            check_if_bool_matrix = if_bool_matrix  # Alias for readability.
            check_if_bool_matrix(matrix, "matrix")
    except TypeError:
        raise TypeError(err_msg)
    except IndexError:
        raise IndexError(err_msg)
    except ValueError:
        raise ValueError(err_msg)
    except BaseException as err:
        raise err

    return None



def if_callable(obj, obj_name):
    r"""Check whether input object is callable.

    If the input object is not callable, then a `TypeError` is raised with the
    message::

        The object ``<obj_name>`` must be callable.

    where <obj_name> is replaced by the contents of the string ``obj_name``.

    Parameters
    ----------
    obj : any type
        Input object.
    obj_name : `str`
        Name of the input object.

    """
    if not callable(obj):
        err_msg = _if_callable_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



###########################
## Define error messages ##
###########################

_if_instance_of_any_accepted_types_err_msg_1 = \
    ("The object ``{}`` must be an instance of the class `{}`.")

_if_instance_of_any_accepted_types_err_msg_2 = \
    ("The object ``{}`` must be an instance of one of the following classes: "
     "{}.")

_if_dict_like_err_msg_1 = \
    ("The object ``{}`` must be dictionary-like.")

_if_str_like_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of strings.")

_if_one_of_any_accepted_strings_err_msg_1 = \
    ("The object ``{}`` must be set to ``'{}'``.")

_if_one_of_any_accepted_strings_err_msg_2 = \
    ("The object ``{}`` must be set to one of the following strings: ``{}``.")

_if_path_like_seq_err_msg_1 = \
    _if_str_like_seq_err_msg_1

_if_int_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of integers.")

_if_positive_int_err_msg_1 = \
    ("The object ``{}`` must be a positive `int`.")

_if_positive_int_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of positive integers.")

_if_nonnegative_int_err_msg_1 = \
    ("The object ``{}`` must be a nonnegative `int`.")

_if_nonnegative_int_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of nonnegative integers.")

_if_multi_dim_slice_like_err_msg_1 = \
    ("The object ``{}`` must be a sequence of items which contains at most one "
     "item being a sequence of integers, and the remaining items being `slice` "
     "objects and/or integers.")

_if_float_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of floating-point numbers.")

_if_positive_float_err_msg_1 = \
    ("The object ``{}`` must be a positive `float`.")

_if_positive_float_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of positive floating-point numbers.")

_if_nonnegative_float_err_msg_1 = \
    ("The object ``{}`` must be a nonnegative `float`.")

_if_nonnegative_float_seq_err_msg_1 = \
    ("The object ``{}`` must be a sequence of nonnegative floating-point "
     "numbers.")

_if_pair_of_floats_err_msg_1 = \
    ("The object ``{}`` must be a pair of real numbers.")

_if_pair_of_positive_floats_err_msg_1 = \
    ("The object ``{}`` must be a pair of positive real numbers.")

_if_pair_of_nonnegative_floats_err_msg_1 = \
    ("The object ``{}`` must be a pair of nonnegative real numbers.")

_if_pair_of_ints_err_msg_1 = \
    ("The object ``{}`` must be a pair of integers.")

_if_pair_of_positive_ints_err_msg_1 = \
    ("The object ``{}`` must be a pair of positive integers.")

_if_pair_of_nonnegative_ints_err_msg_1 = \
    ("The object ``{}`` must be a pair of nonnegative integers.")

_if_quadruplet_of_nonnegative_ints_err_msg_1 = \
    ("The object ``{}`` must be a quadruplet of nonnegative integers.")

_if_pairs_of_floats_err_msg_1 = \
    ("The object ``{}`` must be a sequence of pairs of real numbers.")

_if_real_numpy_array_err_msg_1 = \
    ("The object ``{}`` must be a numpy array of real numbers.")

_if_real_numpy_array_1d_err_msg_1 = \
    ("The object ``{}`` must be a 1D numpy array of real numbers.")

_if_real_numpy_matrix_err_msg_1 = \
    ("The object ``{}`` must be a 2D numpy array of real numbers.")

_if_real_two_column_numpy_matrix_err_msg_1 = \
    ("The object ``{}`` must be a two-column numpy matrix of real numbers.")

_if_real_numpy_array_3d_err_msg_1 = \
    ("The object ``{}`` must be a 3D numpy array of real numbers.")

_if_nonnegative_numpy_array_err_msg_1 = \
    ("The object ``{}`` must be a numpy array of nonnegative numbers.")

_if_nonnegative_numpy_matrix_err_msg_1 = \
    ("The object ``{}`` must be a numpy matrix of nonnegative numbers.")

_if_bool_matrix_err_msg_1 = \
    ("The object ``{}`` must be a boolean matrix.")

_if_bool_array_3d_err_msg_1 = \
    ("The object ``{}`` must be a 3D boolean array.")

_if_callable_err_msg_1 = \
    ("The object ``{}`` must be callable.")
