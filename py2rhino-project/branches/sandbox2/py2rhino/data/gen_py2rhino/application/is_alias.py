is_alias = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "IsAlias",
    "output_package_name": "application",
    "output_module_name": "is_alias",

    "doc_html": """
        Verifies that a command alias exists in Rhino.
    """,

    "syntax_html": {
        0: ("strAlias"),
    },

    "params_html": {
        0: {
            "name": "strAlias",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Alias",
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

    "id_com": 711,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

