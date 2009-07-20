set_document_data = {
    "module_name": "user_data",
    "class_name": "UserData",
    "method_name": "set_document_data",

    "doc_html": """
        Adds or sets a RhinoScript user data item to the current document.
    """,

    "syntax_html": """
        Rhino.SetDocumentData (strSection, strEntry, strValue)
    """,

    "params_html": {
        0: {
            "name": "Section",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The section name.
            """
        },
        1: {
            "name": "Entry",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The entry name.
            """
        },
        2: {
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

    "id_com": 243,

    "params_com": {
        0: {
            "name": "vaApp",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKey",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

