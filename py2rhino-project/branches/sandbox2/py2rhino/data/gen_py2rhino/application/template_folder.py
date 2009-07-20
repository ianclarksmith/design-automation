template_folder = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "TemplateFolder",
    "output_package_name": "application",
    "output_module_name": "template_folder",

    "doc_html": """
        Returns or sets the location of Rhino's template files.
    """,

    "syntax_html": """
        Rhino.TemplateFolder ([strFolder])
    """,

    "params_html": {
        0: {
            "name": "Folder",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The location of Rhino's template files. Note, the location, or folder, must exist.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFolder is not specified, then the current template file folder if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFolder is specified, then the previous template file folder if successful."
        },
    },

    "id_com": 528,

    "params_com": {
        0: {
            "name": "vaFolder",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

