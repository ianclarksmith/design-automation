template_folder = {

    "class": "Application",
    "method": "template_folder",
    "doc": """
        Returns or sets the location of Rhino's template files.
    """,

    "syntax": """
        Rhino.TemplateFolder ([strFolder])
    """,

    "params": {
        0: {
            "name": "folder",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The location of Rhino's template files. Note, the location, or folder, must exist.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If strFolder is not specified, then the current template file folder if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If strFolder is specified, then the previous template file folder if successful."
        },
    }

}

