add_interp_crv_on_srf = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddInterpCrvOnSrf",
    "output_package_name": "curve",
    "output_module_name": "add_interp_crv_on_srf",

    "doc_html": """
        Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoints"),
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
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points that lie on the specified surface. The array must contain at least two points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 513,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

