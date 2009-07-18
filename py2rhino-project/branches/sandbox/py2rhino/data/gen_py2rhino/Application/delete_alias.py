delete_alias = {

    "class": "Application",
    "method": "delete_alias",
    "doc": """
        Deletes an existing command alias from Rhino.
    """,

    "syntax": """
        Rhino.DeleteAlias (strAlias)
    """,

    "params": {
        0: {
            "name": "alias",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of an existing command alias.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

