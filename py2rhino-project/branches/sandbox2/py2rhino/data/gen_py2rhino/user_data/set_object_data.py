set_object_data = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "set_object_data",

    "doc_html": """
        Adds or sets a RhinoScript user data item to an object's geometry.
    """,

    "syntax_html": """
        Rhino.SetObjectData (strObject, strSection, strEntry, strValue)
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
        1: {
            "name": "Section",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The application name.
            """
        },
        2: {
            "name": "Entry",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The key name.
            """
        },
        3: {
            "name": "Value",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The string value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The previous value if successful."
        },
        1: {
            "type": "null",
            "doc": "If no previous value exits, if not successful, or on error."
        },
    },

    "id_com": 244,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaApp",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKey",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

