object_grip_count = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "object_grip_count",

    "doc_html": """
        Returns the number of grips owned by an object.
    """,

    "syntax_html": """
        Rhino.ObjectGripCount (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of grips if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 500,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

