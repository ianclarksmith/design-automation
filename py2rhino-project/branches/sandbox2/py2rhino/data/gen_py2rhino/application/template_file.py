template_file = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "template_file",

    "doc_html": """
        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.
    """,

    "syntax_html": """
        Rhino.TemplateFile ([strFilename])
    """,

    "params_html": {
        0: {
            "name": "Filename",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

