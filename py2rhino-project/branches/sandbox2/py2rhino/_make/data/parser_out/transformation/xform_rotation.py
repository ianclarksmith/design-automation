xform_rotation = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformRotation",
    "output_package_name": "transformation",
    "output_module_name": "xform_rotation",

    "doc_html": """
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    """,

    "syntax_html": {
        0: ("arrPlane1", "arrPlane2"),
        1: ("dblAngle", "arrAxis", "arrPoint"),
        2: ("arrStartDir", "arrEndDir", "arrPoint"),
        3: ("arrX0", "arrY0", "arrZ0", "arrX1", "arrY1", "arrZ1"),
    },

    "params_html": {
        0: {
            "name": "arrPlane1",
            "py_name": "plane_1",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane1",
            "doc": """
        The starting plane.
            """
        },
        1: {
            "name": "arrPlane2",
            "py_name": "plane_2",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane2",
            "doc": """
        The ending plane.
            """
        },
        2: {
            "name": "dblAngle",
            "py_name": "angle",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The rotation angle in degrees.
            """
        },
        3: {
            "name": "arrAxis",
            "py_name": "axis",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Axis",
            "doc": """
        The rotation axis.
            """
        },
        4: {
            "name": "arrStartDir",
            "py_name": "start_dir",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartDir",
            "doc": """
        The starting direction.
            """
        },
        5: {
            "name": "arrEndDir",
            "py_name": "end_dir",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndDir",
            "doc": """
        The ending direction.
            """
        },
        6: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array (3-D Point)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The rotation center point.
            """
        },
        7: {
            "name": "arrX0",
            "py_name": "x_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "X0",
            "doc": """
        The initial frame X
            """
        },
        8: {
            "name": "arrY0",
            "py_name": "y_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Y0",
            "doc": """
        The initial frame Y.
            """
        },
        9: {
            "name": "arrZ0",
            "py_name": "z_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Z0",
            "doc": """
        The initial frame Z.
            """
        },
        10: {
            "name": "arrX1",
            "py_name": "x_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "X1",
            "doc": """
        The final frame X.
            """
        },
        11: {
            "name": "arrY1",
            "py_name": "y_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Y1",
            "doc": """
        The final frame Y.
            """
        },
        12: {
            "name": "arrZ1",
            "py_name": "z_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Z1",
            "doc": """
        The final frame Z.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 794,

    "params_com": {
        0: {
            "name": "va0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "va1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "va2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "va3",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "va4",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "va5",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

