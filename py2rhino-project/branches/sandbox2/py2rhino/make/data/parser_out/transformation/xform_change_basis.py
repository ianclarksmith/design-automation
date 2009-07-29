xform_change_basis = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformChangeBasis",
    "output_package_name": "transformation",
    "output_module_name": "xform_change_basis",

    "doc_html": """
        Returns a change of basis transformation matrix.
    """,

    "syntax_html": {
        0: ("arrPlane1", "arrPlane2"),
        1: ("arrX0", "arrY0", "arrZ0", "arrX1", "arrY1", "arrZ1"),
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
        The initial plane.
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
        The final plane.
            """
        },
        2: {
            "name": "arrX0",
            "py_name": "x_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "X0",
            "doc": """
        The initial basis X (X0,Y0,Z0 can be any 3-D basis)
            """
        },
        3: {
            "name": "arrY0",
            "py_name": "y_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Y0",
            "doc": """
        The  initial basis Y
            """
        },
        4: {
            "name": "arrZ0",
            "py_name": "z_0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Z0",
            "doc": """
        The  initial basis Z
            """
        },
        5: {
            "name": "arrX1",
            "py_name": "x_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "X1",
            "doc": """
        The final basis X (X1,Y1,Z1 can be any 3-D basis)
            """
        },
        6: {
            "name": "arrY1",
            "py_name": "y_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Y1",
            "doc": """
        The  final basis Y
            """
        },
        7: {
            "name": "arrZ1",
            "py_name": "z_1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr_of_dbl",
            "name_main": "Z1",
            "doc": """
        The final basis Z
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 796,

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

