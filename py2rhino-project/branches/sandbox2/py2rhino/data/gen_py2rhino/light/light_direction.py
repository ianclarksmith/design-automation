light_direction = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "LightDirection",
    "output_package_name": "light",
    "output_module_name": "light_direction",

    "doc_html": """
        Returns or changes the direction of a light object. This function can be used to return or modify the target of spotlights.
    """,

    "syntax_html": """
        Rhino.LightDirection (strObject [, arrDirection])
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
        1: {
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The new end point, or direction.  If omitted, the direction point is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If a direction point is not specified,  the current direction if successful."
        },
        1: {
            "type": "array",
            "doc": "If a direction point is specified, the previous direction point if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 491,

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

