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
__all__ = []



def to_dict(obj, obj_name):
    if isinstance(obj, dict):
        result = obj
    else:
        czekitout.check.if_dict_like(obj, obj_name)
        result = dict(obj)

    return result



def to_str_from_str_like(obj, obj_name):
    if isinstance(obj, str):
        result = obj
    else:
        czekitout.check.if_str_like(obj, obj_name)
        result = str(obj)

    return result



def to_str_from_path_like(obj, obj_name):
    czekitout.check.if_path_like(obj, obj_name)
    result = str(obj)

    return result



def to_multi_dim_slice(obj, obj_name):
    czekitout.check.if_multi_dim_slice(obj, obj_name)
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
    czekitout.check.if_int_seq(obj, obj_name)
    result = list(int(num) for num in obj)

    return result



def to_tuple_of_ints(obj, obj_name):
    czekitout.check.if_int_seq(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_pair_of_floats(obj, obj_name):
    czekitout.check.if_pair_of_floats(obj, obj_name)
    result = tuple(float(num) for num in obj)

    return result



def to_pair_of_positive_ints(obj, obj_name):
    czekitout.check.if_pair_of_positive_ints(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_pair_of_nonnegative_ints(obj, obj_name):
    czekitout.check.if_pair_of_nonnegative_ints(obj, obj_name)
    result = tuple(int(num) for num in obj)

    return result



def to_real_two_column_numpy_matrix(obj, obj_name):
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
    czekitout.check.if_bool(obj, obj_name)
    result = bool(int(obj))

    return result



def to_float(obj, obj_name):
    czekitout.check.if_float(obj, obj_name)
    result = float(obj)

    return result



def to_int(obj, obj_name):
    czekitout.check.if_int(obj, obj_name)
    result = int(obj)

    return result



def to_positive_float(obj, obj_name):
    czekitout.check.if_positive_float(obj, obj_name)
    result = float(obj)

    return result



def to_positive_int(obj, obj_name):
    czekitout.check.if_positive_int(obj, obj_name)
    result = int(obj)

    return result



def to_numpy_array(obj, obj_name):
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
    if czekitout.isa.bool_numpy_matrix(obj):
        result = obj
    else:
        czekitout.check.if_bool_matrix(obj, obj_name)
        result = np.array(obj, dtype=bool)

    return result



def to_bool_numpy_array_3d(obj, obj_name):
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
    ("The parameter ``{}`` must be two-column matrix of real numbers.")

_to_numpy_array_err_msg_1 = \
    ("The parameter ``{}`` must be an array.")

_to_real_numpy_matrix_err_msg_1 = \
    ("The parameter ``{}`` must be a real-valued matrix.")

_to_real_numpy_array_3d_err_msg_1 = \
    ("The parameter ``{}`` must be a real-valued three-dimensional array.")

