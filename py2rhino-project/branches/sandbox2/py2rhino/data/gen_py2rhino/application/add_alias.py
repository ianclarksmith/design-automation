add_alias = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "add_alias",

    "doc_html": """
        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.
    """,

    "syntax_html": """
        Rhino.AddAlias (strAlias, strMacro)
    """,

    "params_html": {
        0: {
            "name": "Alias",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new command alias. The name cannot match command names or existing aliases.
            """
        },
        1: {
            "name": "Macro",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The macro to run when the alias is executed.
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

    "id_com": 709,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMacro",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

