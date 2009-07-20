is_linear_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "IsLinearLight",
    "output_package_name": "light",
    "output_module_name": "is_linear_light",

    "doc_html": """
        Verifies a light object is a linear light.
    """,

    "syntax_html": """
        Rhino.IsLinearLight (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The light object's identifier.
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

    "id_com": 163,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

