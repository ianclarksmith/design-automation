is_dimension = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "IsDimension",
    "output_package_name": "dimension",
    "output_module_name": "is_dimension",

    "doc_html": """
        Verifies an object is a dimension object.
    """,

    "syntax_html": """
        Rhino.IsDimension (strObject)
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

    "id_com": 564,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

