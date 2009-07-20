dimension_text = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimensionText",
    "output_package_name": "dimension",
    "output_module_name": "dimension_text",

    "doc_html": """
        Returns the text displayed by a dimension object.
    """,

    "syntax_html": """
        Rhino.DimensionText (strObject)
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
            "type": "string",
            "doc": "The dimension text if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 469,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

