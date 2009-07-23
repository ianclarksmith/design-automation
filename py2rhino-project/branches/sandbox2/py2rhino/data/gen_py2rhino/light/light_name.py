light_name = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "LightName",
    "output_package_name": "light",
    "output_module_name": "light_name",

    "doc_html": """
        Returns or modifies the user-definable name of a light object.
    """,

    "syntax_html": {
        0: ("strObject", "strName"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the light object.
            """
        },
        1: {
            "name": "strName",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
            "doc": """
        The new light name.  If omitted, the current light name is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strName is not specified,  the current light name if successful."
        },
        1: {
            "type": "string",
            "doc": "If strName is specified,  the previous light name if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 169,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

