xform_change_basis = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformChangeBasis",
    "output_package_name": "transformation",
    "output_module_name": "xform_change_basis",

    "doc_html": """
        Returns a change of basis transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformChangeBasis (arrPlane1, arrPlane2)
    """,

    "params_html": {
        0: {
            "name": "Plane1",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The initial plane.
            """
        },
        1: {
            "name": "Plane2",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The final plane.
            """
        },
        2: {
            "name": "X0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The initial basis X (X0,Y0,Z0 can be any 3-D basis)
            """
        },
        3: {
            "name": "Y0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The  initial basis Y
            """
        },
        4: {
            "name": "Z0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The  initial basis Z
            """
        },
        5: {
            "name": "X1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The final basis X (X1,Y1,Z1 can be any 3-D basis)
            """
        },
        6: {
            "name": "Y1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The  final basis Y
            """
        },
        7: {
            "name": "Z1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
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

