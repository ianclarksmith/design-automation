point_scale = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "point_scale",

    "doc_html": """
        Scales a 3-D point.
    """,

    "syntax_html": """
        Rhino.PointScale (arrPoint, dblScale)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point to scale.
            """
        },
        1: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The scale factor to apply.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 669,

    "params_com": {
        0: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

