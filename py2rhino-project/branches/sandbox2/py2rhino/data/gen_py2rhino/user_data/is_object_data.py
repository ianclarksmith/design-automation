is_object_data = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "is_object_data",

    "doc_html": """
        Verifies that an object's geometry contains RhinoScript user data.
    """,

    "syntax_html": """
        Rhino.IsObjectData (strObject)
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
            "type": "boolean",
            "doc": "True or False indicating whether or not the object's geometry contains any RhinoScript user data if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 279,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

