osnap = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "Osnap",
    "output_package_name": "application",
    "output_module_name": "osnap",

    "doc_html": """
        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.
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
            "doc": "If blnEnable is not specified, then the current object snap status if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is specified, then the previous object snap status if successful."
        },
    },

    "id_com": 347,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

