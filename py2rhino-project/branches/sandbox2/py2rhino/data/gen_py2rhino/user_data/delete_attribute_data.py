delete_attribute_data = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "delete_attribute_data",

    "doc_html": """
        Removes RhinoScript user data items from an object's attributes.
    """,

    "syntax_html": """
        Rhino.DeleteAttributeData (strObject [, strSection [, strEntry]])
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
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The section name.  If omitted, all sections and their corresponding entries are removed.
            """
        },
        2: {
            "name": "Entry",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The entry name.  If omitted, all entries for strSection are removed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 684,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaApp",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKey",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

