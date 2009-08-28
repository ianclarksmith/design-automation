alias_macro = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AliasMacro",
    "output_package_name": "application",
    "output_module_name": "alias_macro",

    "doc_html": """
        Returns or modifies the macro of a command alias.
    """,

    "syntax_html": {
        0: ("strAlias", "strMacro"),
    },

    "params_html": {
        0: {
            "name": "strAlias",
            "py_name": "alias",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Alias",
            "doc": """
        The name of an existing command alias.
            """
        },
        1: {
            "name": "strMacro",
            "py_name": "macro",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Macro",
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

