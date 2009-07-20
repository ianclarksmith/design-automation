xform_scale = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_scale",

    "doc_html": """
        Returns a scale transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformScale (arrPlane, dblXScale, dblYScale, dblZScale)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The starting plane.
            """
        },
        1: {
            "name": "XScale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The scale factor in the x-axis direction.
            """
        },
        2: {
            "name": "YScale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The scale factor in the y-axis direction.
            """
        },
        3: {
            "name": "ZScale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The scale factor in the z-axis direction.
            """
        },
        4: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The ending direction.
            """
        },
        5: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array (3-D Point)",
            "type_string": "arr",
            "doc": """
        The rotation center point.
            """
        },
        6: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "dbl",
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

