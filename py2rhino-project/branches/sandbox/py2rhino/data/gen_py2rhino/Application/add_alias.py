add_alias = {

    "class": "Application",
    "method": "add_alias",
    "doc": """
        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.
    """,

    "syntax": """
        Rhino.AddAlias (strAlias, strMacro)
    """,

    "params": {
        0: {
            "name": "alias",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of the new command alias. The name cannot match command names or existing aliases.
            """
        },
        1: {
            "name": "macro",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The macro to run when the alias is executed.
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
            "doc": "On error."
        },
    }

}

