template_file = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "TemplateFile",
    "output_package_name": "application",
    "output_module_name": "template_file",

    "doc_html": """
        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.
    """,

    "syntax_html": {
        0: ("strFilename"),
    },

    "params_html": {
        0: {
            "name": "strFilename",
            "py_name": "filename",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Filename",
            "doc": """
        The name of the new default template file. Note, the template file must exist.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFilename is not specified, then the current default template file if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFilename is specified, then the previous default template file if successful."
        },
    },

    "id_com": 529,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

