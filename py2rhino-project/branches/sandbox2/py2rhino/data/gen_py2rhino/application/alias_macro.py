alias_macro = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AliasMacro",
    "output_package_name": "application",
    "output_module_name": "alias_macro",

    "doc_html": """
        Returns or modifies the macro of a command alias.
    """,

    "syntax_html": """
        Rhino.AliasMacro (strAlias [, strMacro])
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
        1: {
            "name": "Macro",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new macro to run when the alias is executed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a new macro is not specified,  the existing macro if successful."
        },
        1: {
            "type": "string",
            "doc": "If a new macro is specified, the previous macro if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 708,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMacro",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

