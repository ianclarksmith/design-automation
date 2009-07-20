is_text = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "IsText",
    "output_package_name": "geometry",
    "output_module_name": "is_text",

    "doc_html": """
        Verifies an object is a text object.
    """,

    "syntax_html": """
        Rhino.IsText (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 122,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

