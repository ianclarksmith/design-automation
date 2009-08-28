light_location = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "LightLocation",
    "output_package_name": "light",
    "output_module_name": "light_location",

    "doc_html": """
        Returns or changes the location of a light object.
    """,

    "syntax_html": {
        0: ("strObject", "arrlocation"),
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
        The light object's identifier.
            """
        },
        1: {
            "name": "arrlocation",
            "py_name": "location",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "location",
            "doc": """
        The new start point, or location.  If omitted, the location point is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If a location point is not specified,  the current location if successful."
        },
        1: {
            "type": "array",
            "doc": "If a location point is specified, the previous location point if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 490,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

