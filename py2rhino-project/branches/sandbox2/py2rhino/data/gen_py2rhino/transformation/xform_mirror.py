xform_mirror = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_mirror",

    "doc_html": """
        Creates a mirror transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformMirror (arrPoint, arrNormal)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point on mirror plane.
            """
        },
        1: {
            "name": "Normal",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D vector that is normal to mirror plane.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 795,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNormal",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

