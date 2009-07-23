attribute_data_count = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "AttributeDataCount",
    "output_package_name": "user_data",
    "output_module_name": "attribute_data_count",

    "doc_html": """
        Returns the number of RhinoScript user data items on an object's attributes.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of RhinoScript object user data items if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 685,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

