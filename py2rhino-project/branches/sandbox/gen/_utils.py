def flatten(arr):
    """helper method to flatten any arrays into one-dimensional arrays compatible with RhinoScript"""
    if isinstance(arr, (list, tuple)):
        arr_out = []
        for val in arr:
            if isinstance(val, (list, tuple)):
                arr_out += (flatten_once(val))
            else:
                arr_out.append(val)
        return arr_out
    else:
        return [arr]

def flatten_once(arr):
    """helper method to flatten 2-dim arrays into one-dimensional arrays compatible with RhinoScript"""
    if isinstance(arr, (list, tuple)):
        arr_out = []
        for val in arr:
            if isinstance(val, (list, tuple)):
                arr_out += val
            else:
                arr_out.append(val)
        return arr_out
    else:
        return [arr]
