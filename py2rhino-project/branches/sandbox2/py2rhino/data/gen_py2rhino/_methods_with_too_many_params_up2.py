#These methods have too many parameters when compared to the COM definition

application = {
},
block = {
    "insert_block": {
    	# The COM object lists the following parameters
    	# 0: vaName, Required
    	# 1: vaPt, Required
    	# 2: vaScale, Optional
    	# 3: vaAngle, Optional
    	# 4: vaRotate, Optional
        
        "SPLIT_METHOD:": {
            "insert_block": {
                "Name":     ("Required", "str"),
                "Point":     ("Required", "arr_of_???"),
                "Scale":     ("Optional", "arr_of_???"),
                "Angle":     ("Optional", "dbl"),
                "Normal":     ("Optional", "arr_of_???"),
            },
            "insert_block_xform": {
                "Name":     ("Required", "str"),        
                "Xform":     ("Required", "arr_of_???"),
            }
        }        
    },
},
curve = {
    "curve_knot_count": { #<<<<<<<<<<<<<<<< OK
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        "Object": 	("Required", "str"),
        "Index": 	("Optional", "int"),
    },
    "curve_knots": {#<<<<<<<<<<<<<<<< OK
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        "Object": 	("Required", "str"),
        "Index": 	("Optional", "int"),
    },
    "offset_curve_on_surface": {
    	# The COM object lists the following parameters
    	# 0: vaCurve, Required
    	# 1: vaSurface, Required
    	# 2: vaDistance, Required
        "Curve": 	("Required", "str"),
        "Surface": 	("Required", "str"),
        "Distance": 	("Required", "dbl"),
        "Parameter": 	("Required", "arr_of_???"),
    },
},
dimension = {
},
document = {
},
geometry = {
    "add_text": {
    	# The COM object lists the following parameters
    	# 0: vaText, Required
    	# 1: vaPoint, Required
    	# 2: vaHeight, Optional
    	# 3: vaFont, Optional
    	# 4: vaStyle, Optional
        "Text": 	("Required", "str"),
        "Point": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Height": 	("Optional", "dbl"),
        "Font": 	("Optional", "str"),
        "Style": 	("Optional", "int"),
    },
},
group = {
},
hatch = {
},
layer = {
},
light = {
},
line_and_plane = {
    "line_is_farther_than": {
    	# The COM object lists the following parameters
    	# 0: vaLine, Required
    	# 1: vaDist, Required
    	# 2: vaPoints, Required
        "Line": 	("Required", "arr_of_???"),
        "Distance": 	("Required", "dbl"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
    "line_max_distance_to": {
    	# The COM object lists the following parameters
    	# 0: vaLine, Required
    	# 1: vaPoints, Required
        "Line": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
    "line_min_distance_to": {
    	# The COM object lists the following parameters
    	# 0: vaLine, Required
    	# 1: vaPoints, Required
        "Line": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
},
linetype = {
},
material = {
    "match_material": {
    	# The COM object lists the following parameters
    	# 0: vaSrc, Required
    	# 1: vaDest, Required
        "SrcMaterialIndex": 	("Required", "int"),
        "SrcObject": 	("Required", "str"),
        "DestObjects": 	("Required", "arr_of_???"),
    },
},
math = {
    "distance": {#<<<<<<<<<<<<<<<< OK
    	# The COM object lists the following parameters
    	# 0: vaFrom, Required
    	# 1: vaTo, Required
        
        "Point1": 	("Required", "arr_of_???"),
        #"Point2": 	("Required", "arr_of_???"),
        "PointArray": 	("Required", "arr_of_???"),
    },
},
mesh = {
    "mesh_vertex_colors": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaColors, Optional
        "Object": 	("Required", "str"),
        "VertexColors": 	("Optional", "arr_of_???"),
        "Null": 	("Optional", "arr_of_???"),
    },
},
object = {
    "copy_objects": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaStart, Optional
    	# 2: vaEnd, Optional
        "Objects": 	("Required", "arr_of_???"),
        "Start": 	("Optional", "arr_of_???"),
        "End": 	("Optional", "arr_of_???"),
        "Translation": 	("Optional", "arr_of_???"),
    },
    "move_objects": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaStart, Required
    	# 2: vaEnd, Optional
        "Objects": 	("Required", "arr_of_???"),
        "Start": 	("Required", "arr_of_???"),
        "End": 	("Required", "arr_of_???"),
        "Translation": 	("Required", "arr_of_???"),
    },
    "transform_objects": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaXform, Required
        "Objects": 	("Required", "arr_of_???"),
        "Matrix": 	("Required", "arr_of_???"),
        "Copy": 	("Optional", "bln"),
    },
},
object_grip = {
},
point_and_vector = {
},
selection = {
},
surface_and_polysurface = {
    "add_cone": {
    	# The COM object lists the following parameters
    	# 0: vaCenter, Required
    	# 1: vaHeight, Required
    	# 2: vaRadius, Required
    	# 3: vaCap, Optional
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Height": 	("Required", "arr_of_???"),
        "Height": 	("Required", "dbl"),
        "Radius": 	("Required", "dbl"),
        "Cap": 	("Optional", "bln"),
    },
    "add_cylinder": {
    	# The COM object lists the following parameters
    	# 0: vaCenter, Required
    	# 1: vaHeight, Required
    	# 2: vaRadius, Required
    	# 3: vaCap, Optional
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Height": 	("Required", "arr_of_???"),
        "Height": 	("Required", "dbl"),
        "Radius": 	("Required", "dbl"),
        "Cap": 	("Optional", "bln"),
    },
    "add_sphere": {
    	# The COM object lists the following parameters
    	# 0: vaCenter, Required
    	# 1: vaRadius, Required
        "Center": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Radius": 	("Required", "dbl"),
    },
    "add_srf_contour_crvs": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: va0, Required
    	# 2: va1, Optional
    	# 3: va2, Optional
        "Object": 	("Required", "str"),
        "StartPoint": 	("Required", "arr_of_???"),
        "EndPoint": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Interval": 	("Optional", "dbl"),
    },
    "add_torus": {
    	# The COM object lists the following parameters
    	# 0: vaCenter, Required
    	# 1: vaRadius1, Required
    	# 2: vaRadius2, Required
    	# 3: vaDirection, Optional
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "MajorRadius": 	("Required", "dbl"),
        "MinorRadius": 	("Required", "dbl"),
        "Direction": 	("Optional", "arr_of_???"),
    },
},
transformation = {
    "xform_change_basis": {
    	# The COM object lists the following parameters
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
    	# 4: va4, Optional
    	# 5: va5, Optional
        "Plane1": 	("Required", "arr_of_???"),
        "Plane2": 	("Required", "arr_of_???"),
        "X0": 	("Required", "arr_of_???"),
        "Y0": 	("Required", "arr_of_???"),
        "Z0": 	("Required", "arr_of_???"),
        "X1": 	("Required", "arr_of_???"),
        "Y1": 	("Required", "arr_of_???"),
        "Z1": 	("Required", "arr_of_???"),
    },
    "xform_rotation": {
    	# The COM object lists the following parameters
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
    	# 4: va4, Optional
    	# 5: va5, Optional
        "Plane1": 	("Required", "arr_of_???"),
        "Plane2": 	("Required", "arr_of_???"),
        "Angle": 	("Required", "dbl"),
        "Axis": 	("Required", "arr_of_???"),
        "StartDir": 	("Required", "arr_of_???"),
        "EndDir": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "X0": 	("Required", "arr_of_???"),
        "Y0": 	("Required", "arr_of_???"),
        "Z0": 	("Required", "arr_of_???"),
        "X1": 	("Required", "arr_of_???"),
        "Y1": 	("Required", "arr_of_???"),
        "Z1": 	("Required", "arr_of_???"),
    },
    "xform_scale": {
    	# The COM object lists the following parameters
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
        "Plane": 	("Required", "arr_of_???"),
        "XScale": 	("Required", "dbl"),
        "YScale": 	("Required", "dbl"),
        "ZScale": 	("Required", "dbl"),
        "Vector": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "Scale": 	("Required", "dbl"),
    },
},
user_data = {
},
user_interface = {
},
utility = {
    "make_array": {
    	# The COM object lists the following parameters
    	# 0: vaRGB, Required
        "UpperBound": 	("Required", "n"),
        "vVariant": 	("Optional", "n"),
    },
},
view = {
},
