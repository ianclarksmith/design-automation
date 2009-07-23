is_object_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "IsObjectData",
    "output_package_name": "user_data",
    "output_module_name": "is_object_data",

    "doc_html": """
        Verifies that an object's geometry contains RhinoScript user data.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
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
            "type": "boolean",
            "doc": "True or False indicating whether or not the object's geometry contains any RhinoScript user data if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 279,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

