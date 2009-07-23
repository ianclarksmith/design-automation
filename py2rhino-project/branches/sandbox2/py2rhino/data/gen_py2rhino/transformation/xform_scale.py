xform_scale = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformScale",
    "output_package_name": "transformation",
    "output_module_name": "xform_scale",

    "doc_html": """
        Returns a scale transformation matrix.
    """,

    "syntax_html": {
        0: ("arrPlane", "dblXScale", "dblYScale", "dblZScale"),
        1: ("dblXScale", "dblYScale", "dblZScale"),
        2: ("arrVector"),
        3: ("arrPoint", "dblScale"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "name_prefix": "arr",
            "name_main": "Plane",
            "doc": """
        The starting plane.
            """
        },
        1: {
            "name": "dblXScale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "XScale",
            "doc": """
        The scale factor in the x-axis direction.
            """
        },
        2: {
            "name": "dblYScale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "YScale",
            "doc": """
        The scale factor in the y-axis direction.
            """
        },
        3: {
            "name": "dblZScale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "ZScale",
            "doc": """
        The scale factor in the z-axis direction.
            """
        },
        4: {
            "name": "arrVector",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "arr",
            "name_main": "Vector",
            "doc": """
        The ending direction.
            """
        },
        5: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array (3-D Point)",
            "name_prefix": "arr",
            "name_main": "Point",
            "doc": """
        The rotation center point.
            """
        },
        6: {
            "name": "dblScale",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The initial frame X
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

    "id_com": 790,

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

