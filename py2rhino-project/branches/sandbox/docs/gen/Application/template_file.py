template_file = {

    "class": "Application",
    "method": "template_file",
    "doc": """
        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.
    """,

    "syntax": """
        Rhino.TemplateFile ([strFilename])
    """,

    "params": {
        0: {
            "name": "filename",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of the new default template file. Note, the template file must exist.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If strFilename is not specified, then the current default template file if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If strFilename is specified, then the previous default template file if successful."
        },
    }

}

