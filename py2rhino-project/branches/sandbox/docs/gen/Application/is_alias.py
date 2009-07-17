is_alias = {

    "class": "Application",
    "method": "is_alias",
    "doc": """
        Verifies that a command alias exists in Rhino.
    """,

    "syntax": """
        Rhino.IsAlias (strAlias)
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

