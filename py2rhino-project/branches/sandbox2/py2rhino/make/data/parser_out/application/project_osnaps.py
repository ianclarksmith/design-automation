project_osnaps = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "ProjectOsnaps",
    "output_package_name": "application",
    "output_module_name": "project_osnaps",

    "doc_html": """
        Enables or disables object snap projection.
    """,

    "syntax_html": {
        0: ("blnEnable"),
    },

    "params_html": {
        0: {
            "name": "blnEnable",
            "py_name": "enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Enable",
            "doc": """
        The new enabled status, either True or False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current object snap projection status if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is specified, then the previous object snap projection status if successful."
        },
    },

    "id_com": 348,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

