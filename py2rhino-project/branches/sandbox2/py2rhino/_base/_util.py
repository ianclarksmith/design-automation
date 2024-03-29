import pythoncom
#------------------------------------------------------------------------------ 
# Copied from comtypes\automation.py
# VARIANT, in all it's glory.

VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29
VT_LPSTR = 30
VT_LPWSTR = 31
VT_RECORD = 36
VT_INT_PTR = 37
VT_UINT_PTR = 38
VT_FILETIME = 64
VT_BLOB = 65
VT_STREAM = 66
VT_STORAGE = 67
VT_STREAMED_OBJECT = 68
VT_STORED_OBJECT = 69
VT_BLOB_OBJECT = 70
VT_CF = 71
VT_CLSID = 72
VT_VERSIONED_STREAM = 73
VT_BSTR_BLOB = 4095
VT_VECTOR = 4096
VT_ARRAY = 8192
VT_BYREF = 16384
VT_RESERVED = 32768
VT_ILLEGAL = 65535
VT_ILLEGALMASKED = 4095
VT_TYPEMASK = 4095
#------------------------------------------------------------------------------ 
def flatten_params(params):
    """helper method to flatten any arrays into one-dimensional arrays compatible with RhinoScript"""
    if params == None:
        return None
    if params == pythoncom.Empty:
        return pythoncom.Empty
    elif isinstance(params, (list, tuple)):
        flat_params = ()
        for val in params:
            if isinstance(val, tuple):
                flat_params += val
            elif isinstance(val, list):
                flat_params += tuple(val)
            else:
                flat_params += (val,)
        return flat_params
    else:
        return (params,)
#------------------------------------------------------------------------------ 
"""
def select_params(params, params_required, params_magic_numbers, params_flattened):
    tmp_params_magic_numbers = []
    tmp_params_flattened = []
    
    for i in range(len(params)):
        #check if the values should be added
        add_param = False
        if params_required[i]:
            add_param = True
        else:
            if params[i] != None:
                add_param = True
            #if params_magic_numbers[i][0] == VT_BOOL:
            #    add_param = True
            #    params_flattened[i] = False
        if add_param:
            tmp_params_magic_numbers.append(params_magic_numbers[i])
            tmp_params_flattened.append(params_flattened[i])
        else:
            tmp_params_magic_numbers.append(params_magic_numbers[i])
            tmp_params_flattened.append(pythoncom.Empty)          
    return (tuple(tmp_params_magic_numbers), tuple(tmp_params_flattened))
"""
#===============================================================================
# Run some test
#===============================================================================
if __name__ == '__main__':
    print flatten_params([[1,[2,3]],[4,5,6]])
    print flatten_params(((1,(2,3)),(4,5,6)))
    print flatten_params((4,5,6))
    print flatten_params(None)

