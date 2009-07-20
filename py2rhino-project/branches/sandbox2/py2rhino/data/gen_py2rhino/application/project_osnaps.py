project_osnaps = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "ProjectOsnaps",
    "output_package_name": "application",
    "output_module_name": "project_osnaps",

    "doc_html": """
        Enables or disables object snap projection.
    """,

    "syntax_html": """
        Rhino.ProjectOsnaps ([blnEnable])
    """,

    "params_html": {
        0: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

