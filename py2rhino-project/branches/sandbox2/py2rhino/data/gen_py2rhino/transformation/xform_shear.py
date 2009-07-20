xform_shear = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformShear",
    "output_package_name": "transformation",
    "output_module_name": "xform_shear",

    "doc_html": """
        Returns a scale transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformShear (arrPlane, arrX1, arrY1, arrZ1)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The plane, where arrPlane(0) is the fixed point.
            """
        },
        1: {
            "name": "X1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The x-axis scale factor.
            """
        },
        2: {
            "name": "Y1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The y-axis scale factor.
            """
        },
        3: {
            "name": "Z1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The z-axis scale factor.
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

    "id_com": 791,

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
    },

    "returns_com": "tagVARIANT",

}

