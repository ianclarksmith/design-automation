xform_planar_projection = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_planar_projection",

    "doc_html": """
        Returns a transformation matrix that projects to a plane.
    """,

    "syntax_html": """
        Rhino.XformPlanarProjection (arrPlane)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane to project to.
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

    "id_com": 793,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

