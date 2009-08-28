snap = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "Snap",
    "output_package_name": "application",
    "output_module_name": "snap",

    "doc_html": """
        Enables or disables Rhino's grid snap modeling aid.
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
        The new enabled status, either True or False
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current grid snap status if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is specified, then the previous grid snap status if successful."
        },
    },

    "id_com": 344,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

