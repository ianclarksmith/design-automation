add_alias = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AddAlias",
    "output_package_name": "application",
    "output_module_name": "add_alias",

    "doc_html": """
        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.
    """,

    "syntax_html": {
        0: ("strAlias", "strMacro"),
    },

    "params_html": {
        0: {
            "name": "strAlias",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Alias",
            "doc": """
        The name of the new command alias. The name cannot match command names or existing aliases.
            """
        },
        1: {
            "name": "strMacro",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Macro",
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

