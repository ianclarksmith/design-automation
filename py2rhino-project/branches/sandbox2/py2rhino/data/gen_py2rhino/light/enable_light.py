enable_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "EnableLight",
    "output_package_name": "light",
    "output_module_name": "enable_light",

    "doc_html": """
        Enables or disables a light object.
    """,

    "syntax_html": """
        Rhino.EnableLight (strObject [, blnEnable])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the light object
            """
        },
        1: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The light's enabled status.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current enabled status if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is specified, then the previous enabled status if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 158,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBool",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

