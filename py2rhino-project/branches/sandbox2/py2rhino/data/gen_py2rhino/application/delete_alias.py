delete_alias = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "delete_alias",

    "doc_html": """
        Deletes an existing command alias from Rhino.
    """,

    "syntax_html": """
        Rhino.DeleteAlias (strAlias)
    """,

    "params_html": {
        0: {
            "name": "Alias",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing command alias.
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
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 710,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

