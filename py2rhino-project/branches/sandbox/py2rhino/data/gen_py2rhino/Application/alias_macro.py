alias_macro = {

    "class": "Application",
    "method": "alias_macro",
    "doc": """
        Returns or modifies the macro of a command alias.
    """,

    "syntax": """
        Rhino.AliasMacro (strAlias [, strMacro])
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
        1: {
            "name": "macro",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The new macro to run when the alias is executed.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If a new macro is not specified,  the existing macro if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If a new macro is specified, the previous macro if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

