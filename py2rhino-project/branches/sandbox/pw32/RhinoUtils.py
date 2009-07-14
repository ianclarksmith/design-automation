def Flatten(arrIn):
        """helper method to flatten any arrays into one-dimensional arrays compatible with RhinoScript"""
        if isinstance(arrIn, (list, tuple)):
                arrOut = []
                for val in arrIn:
                        arrOut += (FlattenOnce(val))
                return arrOut
        else:
                return [arrIn]

def FlattenOnce(arrIn):
        """helper method to flatten 2-dim arrays into one-dimensional arrays compatible with RhinoScript"""
        if isinstance(arrIn, (list, tuple)):
                arrOut = []
                for val in arrIn:
                        arrOut += val#arrOut.extend(val)
                #~ arrOut = reduce(list.__add__, tempList, []) #doesn't work with tuples
                return arrOut
        else:
                return [arrIn]
