is_user_text = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "IsUserText",
    "output_package_name": "user_data",
    "output_module_name": "is_user_text",

    "doc_html": """
        Verifies that an object contains user text. For more details on User Text, see the discussion found in the User Data Methods summary.
    """,

    "syntax_html": """
        Rhino.IsUserText (strObject)
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
            "doc": "0 = no user text; 1 = attribute user text; 2 = geometry user text; 3 = both attribute and geometry user text."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 730,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

