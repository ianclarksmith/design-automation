is_attribute_data = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "is_attribute_data",

    "doc_html": """
        Verifies that an object's attributes contains RhinoScript user data.
    """,

    "syntax_html": """
        Rhino.IsAttributeData (strObject)
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
            "doc": "True or False indicating whether or not the object's attributes contains any RhinoScript user data if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 686,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

