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



# For type-checking objects.
import czekitout.isa



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
__all__ = []



def if_instance_of_accepted_types(obj, obj_name, accepted_types):
    if not isinstance(obj, accepted_types):
        names_of_accepted_types = []
        for accepted_type in accepted_types:
            try:
                names_of_accepted_types.append(accepted_type._child_class_name)
            except:
                names_of_accepted_types.append(accepted_type.__name__)
        names_of_accepted_types = tuple(names_of_accepted_types)
                
        if len(names_of_accepted_types) == 1:
            err_msg = _if_instance_of_accepted_types_err_msg_1
            err_msg = err_msg.format(obj_name, names_of_accepted_types[0])
        else:
            names_of_accepted_types = \
                str(names_of_accepted_types).replace("\'", "`")
            err_msg = _if_instance_of_accepted_types_err_msg_2
            err_msg = err_msg.format(obj_name, names_of_accepted_types)
            
        raise TypeError(err_msg)

    return None



def if_dict_like(obj, obj_name):
    try:
        dict(obj)
    except:
        err_msg = _if_dict_like_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_str_like(obj, obj_name):
    check_if_instance_of_accepted_types = \
        if_instance_of_accepted_types  # Alias for readability.

    accepted_types = (str, bytes)
    check_if_instance_of_accepted_types(obj, obj_name, accepted_types)

    return None



def if_path_like(obj, obj_name):
    try:
        os.path.exists(obj)
    except:
        err_msg = _if_instance_of_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "str")
        raise TypeError(err_msg)

    return None



def if_int(obj, obj_name):
    try:
        if abs(int(obj) - obj) > 1.0e-14:
            raise
    except:
        err_msg = _if_instance_of_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "int")
        raise TypeError(err_msg)

    return None



def if_int_seq(obj, obj_name):
    try:
        for num in obj:
            check_if_int = if_int  # Alias for readability.
            check_if_int(num, "num")
    except:
        err_msg = _if_int_seq_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_positive_int(obj, obj_name):
    check_if_int = if_int  # Alias for readability.
    check_if_int(obj, "obj")
    
    try:
        if int(obj) < 1:
            raise
    except:
        err_msg = _if_positive_int_err_msg_1.format(obj_name)
        raise ValueError(err_msg)

    return None



def if_nonnegative_int(obj, obj_name):
    check_if_int = if_int  # Alias for readability.
    check_if_int(obj, "obj")
    
    try:
        if int(obj) < 0:
            raise
    except:
        err_msg = _if_nonnegative_int_err_msg_1.format(obj_name)
        raise ValueError(err_msg)

    return None



def if_multi_dim_slice(obj, obj_name):
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
        err_msg = _if_multi_dim_slice_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_float(obj, obj_name):
    try:
        float(obj)
    except:
        err_msg = _if_instance_of_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "float")
        raise TypeError(err_msg)

    return None



def if_positive_float(obj, obj_name):
    check_if_float = if_float  # Alias for readability.
    check_if_float(obj, obj_name)
    
    if float(obj) <= 0:
        err_msg = _if_positive_float_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_pair_of_floats(obj, obj_name):
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



def if_pair_of_positive_ints(obj, obj_name):
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



def if_real_two_column_numpy_matrix(obj, obj_name):
    if not czekitout.isa.real_two_column_numpy_matrix(obj):
        err_msg = _if_real_two_column_numpy_matrix_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_real_numpy_array_3d(obj, obj_name):
    if not czekitout.isa.real_numpy_array_3d(obj):
        err_msg = _if_real_numpy_array_3d_err_msg_1.format(obj_name)
        raise TypeError(err_msg)

    return None



def if_bool(obj, obj_name):
    try:
        if not isinstance(obj, bool):
            check_if_int = if_int  # Alias for readability.
            check_if_int(obj, obj_name)
            if (int(obj) != 0) and (int(obj) != 1):
                raise
    except:
        err_msg = _if_instance_of_accepted_types_err_msg_1
        err_msg = err_msg.format(obj_name, "bool")
        raise TypeError(err_msg)

    return None



def if_bool_matrix(obj, obj_name):
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



def if_serializable_rep(obj, obj_name, attr_names, child_class_name):
    czekitout.check.if_dict_like(obj, obj_name)

    for attr_name in attr_names:
        if attr_name not in obj:
            err_msg = _if_serializable_rep_err_msg_1
            err_msg = err_msg.format(child_class_name, obj_name, attr_name)
            raise KeyError(err_msg)

    return None



###########################
## Define error messages ##
###########################

_if_instance_of_accepted_types_err_msg_1 = \
    ("The parameter ``{}`` must be an instance of the class `{}`.")

_if_instance_of_accepted_types_err_msg_2 = \
    ("The parameter ``{}`` must be an instance of one of the following "
     "classes: {}.")

_if_dict_like_err_msg_1 = \
    ("The parameter ``{}`` must be dictionary-like.")

_if_int_seq_err_msg_1 = \
    ("The parameter ``{}`` must be a sequence of integers.")

_if_positive_int_err_msg_1 = \
    ("The parameter ``{}`` must be a positive `int`.")

_if_nonnegative_int_err_msg_1 = \
    ("The parameter ``{}`` must be a nonnegative `int`.")

_if_multi_dim_slice_err_msg_1 = \
    ("The parameter ``{}`` must be a sequence of items which contains at most "
     "one item being an ascending sequence of integers, and the remaining "
     "items being `slice` objects and/or integers.")

_if_positive_float_err_msg_1 = \
    ("The parameter ``{}`` must be a positive `float`.")

_if_pair_of_floats_err_msg_1 = \
    ("The parameter ``{}`` must be a pair of real numbers.")

_if_pair_of_positive_ints_err_msg_1 = \
    ("The parameter ``{}`` must be a pair of positive integers.")

_if_pair_of_nonnegative_ints_err_msg_1 = \
    ("The parameter ``{}`` must be a pair of non-negative integers.")

_if_real_two_column_numpy_matrix_err_msg_1 = \
    ("The parameter ``{}`` must be two-column matrix of real numbers.")

_if_bool_matrix_err_msg_1 = \
    ("The parameter ``{}`` must be a boolean matrix.")

_if_bool_matrix_err_msg_1 = \
    ("The parameter ``{}`` must be a boolean three-dimensional array.")

_if_serializable_rep_err_msg_1 = \
    ("Failed to construct an instance of the class `{}` from the parameter "
     "``{}``, assumed to be a serializable object. The parameter ``data`` is "
     "missing the specification for the attribute ``{}``.")
