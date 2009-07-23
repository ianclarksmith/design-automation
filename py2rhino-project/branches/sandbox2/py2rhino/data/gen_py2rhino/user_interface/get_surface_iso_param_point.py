get_surface_iso_param_point = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetSurfaceIsoParamPoint",
    "output_package_name": "user_interface",
    "output_module_name": "get_surface_iso_param_point",

    "doc_html": """
        Pauses for user input of a point constrained to a surface object.
    """,

    "syntax_html": {
        0: ("strObject", "strMessage"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The surface object's identifier.
            """
        },
        1: {
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of selection information if successful. The elements of the array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 775,

    "params_com": {
        0: {
            "name": "vaBrep",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

