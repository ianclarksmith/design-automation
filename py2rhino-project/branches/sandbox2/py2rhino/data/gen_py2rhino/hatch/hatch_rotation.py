hatch_rotation = {
    "module_name": "hatch",
    "class_name": "Hatch",
    "method_name": "hatch_rotation",

    "doc_html": """
        Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane.
    """,

    "syntax_html": """
        Rhino.HatchRotation (strObject [, dblRotation])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a hatch object.
            """
        },
        1: {
            "name": "Rotation",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The rotation angle in degrees.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a rotation angle is not specified, the current rotation angle if successful."
        },
        1: {
            "type": "number",
            "doc": "If a rotation angle is specified, the previous rotation angle if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 839,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRotation",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

