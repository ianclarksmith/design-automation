is_command = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "IsCommand",
    "output_package_name": "application",
    "output_module_name": "is_command",

    "doc_html": """
        Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.
    """,

    "syntax_html": {
        0: ("strCommandName"),
    },

    "params_html": {
        0: {
            "name": "strCommandName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "CommandName",
            "doc": """
        The command name to test.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 530,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

