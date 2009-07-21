#These methods have too many parameters when compared to the COM definition

application = {
},
block = {
    "insert_block": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaName, Required
    	# 1: vaPt, Required
    	# 2: vaScale, Optional
    	# 3: vaAngle, Optional
    	# 4: vaRotate, Optional
        
        "SPLIT_METHOD:": {
            "insert_block": {
                "Name": 	("Required", "str"),
                "Point": 	("Required", "arr_of_???"),
                "Scale": 	("Optional", "arr_of_???"),
                "Angle": 	("Optional", "dbl"),
                "Normal": 	("Optional", "arr_of_???"),
            },
            "insert_block_xform": {
                "Name":     ("Required", "str"),        
                "Xform": 	("Required", "arr_of_???"),
            }
        }
    },
},
curve = {
    "curve_area": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        #"Object": 	("Required", "str"),#this works with a single id
        "Objects": 	("Required", "arr_of_???"),#this works with VT_VARIANT - both lists and single items work
    },
    "curve_area_centroid": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
    },
    "curve_closest_object": {
    	# The COM object lists the following parameters
    	# 0: vaCurve, Required
    	# 1: vaObjects, Required
        
        "Curve": 	("Required", "str"),
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
    },
    "curve_knot_count": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        "Object": 	("Required", "str"),#this works fine
        "Index": 	("Optional", "int"),#this works fine, but we need to deal with optional arg
    },
    "curve_knots": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        "Object": 	("Required", "str"),
        "Index": 	("Optional", "int"),
    },
    "explode_curves": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaDelete, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Delete": 	("Optional", "bln"),
    },
    "project_curve_to_mesh": {
    	# The COM object lists the following parameters
    	# 0: vaCurves, Required
    	# 1: vaMeshes, Required
    	# 2: vaDirection, Required
        
        #"Curve": 	("Required", "str"),
        "Curves": 	("Required", "arr_of_???"),
        #"Mesh": 	("Required", "str"),
        "Meshes": 	("Required", "arr_of_???"),
        "Direction": 	("Required", "arr_of_???"),
    },
    "project_curve_to_surface": {
    	# The COM object lists the following parameters
    	# 0: vaCurves, Required
    	# 1: vaSurfaces, Required
    	# 2: vaDirection, Required
        
        #"Curve": 	("Required", "str"),
        "Curves": 	("Required", "arr_of_???"),
        #"Surface": 	("Required", "str"),
        "Surfaces": 	("Required", "arr_of_???"),
        "Direction": 	("Required", "arr_of_???"),
    },
    "split_curve": {
    	# The COM object lists the following parameters
    	# 0: vaCrv, Required
    	# 1: vaParam, Required
    	# 2: vaDelete, Optional
        
        "Object": 	("Required", "str"),
        #"Parameter": 	("Required", "dbl"),
        "Parameters": 	("Required", "arr_of_???"),
        "Delete": 	("Optional", "bln"),
    },
},
dimension = {
},
document = {
},
geometry = {
    "add_clipping_plane": {
    	# The COM object lists the following parameters
    	# 0: vaPlane, Required
    	# 1: vaDX, Required
    	# 2: vaDY, Required
    	# 3: vaView, Optional
        
        "Plane": 	("Required", "arr_of_???"),
        "DU": 	("Required", "dbl"),
        "DV": 	("Required", "dbl"),
        #"View": 	("Optional", "str"),
        "Views": 	("Optional", "arr_of_???"),
    },
    "add_text": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaText, Required
    	# 1: vaPoint, Required
    	# 2: vaHeight, Optional
    	# 3: vaFont, Optional
    	# 4: vaStyle, Optional
        
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }        
        
        "Text": 	("Required", "str"),
        "Point": 	("Required", "arr_of_???"),
        "Height": 	("Optional", "dbl"),
        "Font": 	("Optional", "str"),
        "Style": 	("Optional", "int"),
        #or
        #"Text":     ("Required", "str"),
        "Plane":     ("Required", "arr_of_???"),
        #"Height":     ("Optional", "dbl"),
        #"Font":     ("Optional", "str"),
        #"Style":     ("Optional", "int"),        
    },
    "bounding_box": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaView, Optional
    	# 2: vaSystem, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "View": 	("Optional", "str"),
        "WorldCoords": 	("Optional", "bln"),
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
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Line vs Point
    	# 0: vaLine, Required
    	# 1: vaDist, Required
    	# 2: vaPoints, Required

        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }        

        "Line": 	("Required", "arr_of_???"),
        "Distance": 	("Required", "dbl"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
    "line_max_distance_to": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Line vs Point
    	# 0: vaLine, Required
    	# 1: vaPoints, Required

        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }        

        "Line": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
    "line_min_distance_to": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Line vs Point
    	# 0: vaLine, Required
    	# 1: vaPoints, Required
        
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Line": 	("Required", "arr_of_???"),
        "Point": 	("Required", "arr_of_???"),
        "Line2": 	("Required", "arr_of_???"),
    },
},
linetype = {
},
material = {
    "match_material": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaSrc, Required
    	# 1: vaDest, Required
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "SrcMaterialIndex": 	("Required", "int"),
        "SrcObject": 	("Required", "str"),
        #"DestObject": 	("Required", "str"),
        "DestObjects": 	("Required", "arr_of_???"),
    },
},
math = {
    "distance": {
    	# The COM object lists the following parameters
    	# 0: vaFrom, Required
    	# 1: vaTo, Required
        
        "Point1": 	("Required", "arr_of_???"),
        #"Point2": 	("Required", "arr_of_???"),
        "PointArray": 	("Required", "arr_of_???"),
    },
},
mesh = {
    "explode_meshes": {
    	# The COM object lists the following parameters
    	# 0: vaMeshes, Required
    	# 1: vaDelete, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Delete": 	("Optional", "bln"),
    },
    "mesh_area": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
    },
    "mesh_vertex_colors": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObject, Required                            
    	# 1: vaColors, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Object": 	("Required", "str"),
        "VertexColors": 	("Optional", "arr_of_???"),
        "Null": 	("Optional", "arr_of_???"),
    },
    "mesh_volume": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
    },
},
object = {
    "box_morph_object": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaPoints, Required
    	# 2: vaCopy, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "BoxPoints": 	("Required", "arr_of_???"),
        "Copy": 	("Optional", "bln"),
    },
    """
    "copy_object": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObject, Required                            TO BE DELETED
    	# 1: vaStart, Optional
    	# 2: vaEnd, Optional
        
        "Object": 	("Required", "str"),
        "Start": 	("Optional", "arr_of_???"),
        "End": 	("Optional", "arr_of_???"),
        "Translation": 	("Optional", "arr_of_???"),
    },
    """
    "copy_objects": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObjects, Required
    	# 1: vaStart, Optional
    	# 2: vaEnd, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Objects": 	("Required", "arr_of_???"),
        "Start": 	("Optional", "arr_of_???"),
        "End": 	("Optional", "arr_of_???"),
        "Translation": 	("Optional", "arr_of_???"),
    },
    "flash_object": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaStyle, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Style": 	("Optional", "bln"),
    },
    "match_object_attributes": {
    	# The COM object lists the following parameters
    	# 0: vaTarget, Required
    	# 1: vaSource, Optional
        
        #"Target": 	("Required", "str"),
        "Targets": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "str"),
    },
    """
    "move_object": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObject, Required                            TO BE DELETED
    	# 1: vaStart, Required
    	# 2: vaEnd, Optional
        
        "Object": 	("Required", "str"),
        "Start": 	("Required", "arr_of_???"),
        "End": 	("Required", "arr_of_???"),
        "Translation": 	("Required", "arr_of_???"),
    },
    """
    "move_objects": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< XFORM
    	# 0: vaObjects, Required
    	# 1: vaStart, Required
    	# 2: vaEnd, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Objects": 	("Required", "arr_of_???"),
        "Start": 	("Required", "arr_of_???"),
        "End": 	("Required", "arr_of_???"),
        "Translation": 	("Required", "arr_of_???"),
    },
    "object_color": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaValue, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Color": 	("Optional", "lng"),
    },
    "object_color_source": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaValue, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "int"),
    },
    "object_layer": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaLayer, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Layer": 	("Optional", "str"),
    },
    "object_linetype": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaLinetype, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Layer": 	("Optional", "str"),
    },
    "object_linetype_source": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaSource, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "int"),
    },
    "object_material_source": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaValue, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "int"),
    },
    "object_name": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaValue, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Name": 	("Optional", "str"),
    },
    "object_print_color": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaColor, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Color": 	("Optional", "lng"),
    },
    "object_print_color_source": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaSource, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "int"),
    },
    "object_print_width": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vavaWidth, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Width": 	("Optional", "dbl"),
    },
    "object_print_width_source": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaSource, Required
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Source": 	("Optional", "int"),
    },
    "object_u_r_l": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaValue, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "URL": 	("Optional", "str"),
    },
    """
    "transform_object": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObject, Required                            TO BE DELETED
    	# 1: vaXform, Required
        
        "Object": 	("Required", "str"),
        "Matrix": 	("Required", "arr_of_???"),
        "Copy": 	("Optional", "bln"),
    },
    """
    "transform_objects": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    	# 0: vaObjects, Required                            THIS MIGHT WORK
    	# 1: vaXform, Required
        

        "Objects": ("Required", "arr_of_???"),
        "Matrix": ("Required", "arr_of_???"),
        "Copy": ("Optional", "bln"),

        

    },
},
object_grip = {
},
point_and_vector = {
    "project_point_to_mesh": {
    	# The COM object lists the following parameters
    	# 0: vaPoints, Required
    	# 1: vaMeshes, Required
    	# 2: vaDirection, Required
        
        #"Points": 	("Required", "arr_of_???"),
        "Points": 	("Required", "arr_of_???"),
        #"Mesh": 	("Required", "str"),
        "Meshes": 	("Required", "arr_of_???"),
        "Direction": 	("Required", "arr_of_???"),
    },
    "project_point_to_surface": {
    	# The COM object lists the following parameters
    	# 0: vaPoints, Required
    	# 1: vaSurfaces, Required
    	# 2: vaDirection, Required
        
        #"Points": 	("Required", "arr_of_???"),
        "Points": 	("Required", "arr_of_???"),
        #"Surface": 	("Required", "str"),
        "Surfaces": 	("Required", "arr_of_???"),
        "Direction": 	("Required", "arr_of_???"),
    },
},
selection = {
},
surface_and_polysurface = {
    "add_cone": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Plane and Height
    	# 0: vaCenter, Required
    	# 1: vaHeight, Required
    	# 2: vaRadius, Required
    	# 3: vaCap, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Height": 	("Required", "arr_of_???"),
        "Height": 	("Required", "dbl"),
        "Radius": 	("Required", "dbl"),
        "Cap": 	("Optional", "bln"),
    },
    "add_cylinder": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Plane and Height
    	# 0: vaCenter, Required
    	# 1: vaHeight, Required
    	# 2: vaRadius, Required
    	# 3: vaCap, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Height": 	("Required", "arr_of_???"),
        "Height": 	("Required", "dbl"),
        "Radius": 	("Required", "dbl"),
        "Cap": 	("Optional", "bln"),
    },
    "add_sphere": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Plane
    	# 0: vaCenter, Required                            THIS MIGHT WORK
    	# 1: vaRadius, Required
        
        "Center": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Radius": 	("Required", "dbl"),
    },
    "add_srf_contour_crvs": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Plane
    	# 0: vaObject, Required
    	# 1: va0, Required
    	# 2: va1, Optional
    	# 3: va2, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Object": 	("Required", "str"),
        "StartPoint": 	("Required", "arr_of_???"),
        "EndPoint": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "Interval": 	("Optional", "dbl"),
    },
    "add_torus": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Plane
    	# 0: vaCenter, Required
    	# 1: vaRadius1, Required
    	# 2: vaRadius2, Required
    	# 3: vaDirection, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Base": 	("Required", "arr_of_???"),
        "Plane": 	("Required", "arr_of_???"),
        "MajorRadius": 	("Required", "dbl"),
        "MinorRadius": 	("Required", "dbl"),
        "Direction": 	("Optional", "arr_of_???"),
    },
    "explode_polysurfaces": {
    	# The COM object lists the following parameters
    	# 0: vaObjects, Required
    	# 1: vaDelete, Optional
        
        #"Object": 	("Required", "str"),
        "Objects": 	("Required", "arr_of_???"),
        "Delete": 	("Optional", "bln"),
    },
},
transformation = {
    "xform_change_basis": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Plane
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
    	# 4: va4, Optional
    	# 5: va5, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Plane1": 	("Required", "arr_of_???"),
        "Plane2": 	("Required", "arr_of_???"),
        #or
        "X0": 	("Required", "arr_of_???"),
        "Y0": 	("Required", "arr_of_???"),
        "Z0": 	("Required", "arr_of_???"),
        "X1": 	("Required", "arr_of_???"),
        "Y1": 	("Required", "arr_of_???"),
        "Z1": 	("Required", "arr_of_???"),
    },
    "xform_rotation": {
    	# The COM object lists the following parameters  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
    	# 4: va4, Optional
    	# 5: va5, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Plane1": 	("Required", "arr_of_???"),
        "Plane2": 	("Required", "arr_of_???"),
        #or
        "Angle": 	("Required", "dbl"),
        "Axis": 	("Required", "arr_of_???"),
        "Point":     ("Required", "arr_of_???"),
        #or
        "StartDir": 	("Required", "arr_of_???"),
        "EndDir": 	("Required", "arr_of_???"),
        #"Point": 	("Required", "arr_of_???"),
        #or
        "X0": 	("Required", "arr_of_???"),
        "Y0": 	("Required", "arr_of_???"),
        "Z0": 	("Required", "arr_of_???"),
        "X1": 	("Required", "arr_of_???"),
        "Y1": 	("Required", "arr_of_???"),
        "Z1": 	("Required", "arr_of_???"),
    },
    "xform_scale": {
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    	# 0: va0, Required
    	# 1: va1, Optional
    	# 2: va2, Optional
    	# 3: va3, Optional
        
        "SPLIT_METHOD:": {
            "xxx": {

            },
            "yyy": {

            },
            "zzz": {

            }            
        }                
        
        "Plane": 	("Required", "arr_of_???"),
        "XScale": 	("Required", "dbl"),
        "YScale": 	("Required", "dbl"),
        "ZScale": 	("Required", "dbl"),
        #or
        #"XScale":     ("Required", "dbl"),
        #"YScale":     ("Required", "dbl"),
        #"ZScale":     ("Required", "dbl"),
        #or        
        "Vector": 	("Required", "arr_of_???"),
        #or
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
    	# The COM object lists the following parameters <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    	# 0: vaRGB, Required                                THIS PROBABLY WORKS
        
        "UpperBound": 	("Required", "n"),
        "vVariant": 	("Optional", "n"),
    },
},
view = {
},
