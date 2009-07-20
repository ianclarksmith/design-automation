object_data_count = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "object_data_count",

    "doc_html": """
        Returns the number of RhinoScript user data items on an object's geometry.
    """,

    "syntax_html": """
        Rhino.ObjectDataCount (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of RhinoScript object user data items if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 242,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

