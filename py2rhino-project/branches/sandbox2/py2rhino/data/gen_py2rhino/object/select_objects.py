select_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "SelectObjects",
    "output_package_name": "object",
    "output_module_name": "select_objects",

    "doc_html": """
        Selects one or more objects.
    """,

    "syntax_html": """
        Rhino.SelectObjects (arrObjects)
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to select.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects selected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 298,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

