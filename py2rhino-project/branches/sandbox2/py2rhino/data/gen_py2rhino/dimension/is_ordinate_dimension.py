is_ordinate_dimension = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "IsOrdinateDimension",
    "output_package_name": "dimension",
    "output_module_name": "is_ordinate_dimension",

    "doc_html": """
        Verifies an object is an ordinate dimension object.
    """,

    "syntax_html": """
        Rhino.IsOrdinateDimension (strObject)
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

    "id_com": 659,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

