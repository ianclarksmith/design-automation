plane_transform = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "plane_transform",

    "doc_html": """
        Transforms a plane.
    """,

    "syntax_html": """
        Rhino.PlaneTransform (arrPlane, arrXform)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane to transform.
            """
        },
        1: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A valid 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting plane if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 801,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

