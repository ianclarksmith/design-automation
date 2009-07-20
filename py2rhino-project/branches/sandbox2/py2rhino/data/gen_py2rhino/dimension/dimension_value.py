dimension_value = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimensionValue",
    "output_package_name": "dimension",
    "output_module_name": "dimension_value",

    "doc_html": """
        Returns the value of a dimension object.
    """,

    "syntax_html": """
        Rhino.DimensionValue (strObject)
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
            "type": "number",
            "doc": "The value of the dimension successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 568,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

