is_object_valid = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "is_object_valid",

    "doc_html": """
        Verifies that an object's geometry is valid and without error.
    """,

    "syntax_html": """
        Rhino.IsObjectValid (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 522,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

